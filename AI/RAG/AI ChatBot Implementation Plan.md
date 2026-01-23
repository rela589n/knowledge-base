# AI Chatbot Implementation Plan

## Overview

Implement an AI-powered chatbot for customer support and FAQ with:
- Provider-agnostic LLM backend via **Symfony AI** (Claude, OpenAI, Azure, etc.)
- RAG using **ChromaDB** (vector database) + **Chonkie** (semantic chunking)
- Streaming responses via Centrifugo WebSockets
- Function calling for backend actions
- Conversation history persistence

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                         API Layer                                │
│  POST /conversations  │  POST /messages  │  GET /history        │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    Chatbot Module                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ Conversation│  │ Symfony AI  │  │    RAG      │              │
│  │  Manager    │  │  Platform   │  │  Pipeline   │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
│         │                │                │                      │
│  ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐              │
│  │  Messages   │  │  Failover   │  │  ChromaDB   │              │
│  │  (Postgres) │  │  Providers  │  │   Client    │              │
│  └─────────────┘  └─────────────┘  └──────┬──────┘              │
└─────────────────────────────────────────────│───────────────────┘
          │                                   │
          │              ┌────────────────────┼────────────────────┐
          │              │                    │                    │
          │   ┌──────────▼──────────┐  ┌──────▼───────┐            │
          │   │   Chonkie Service   │  │   ChromaDB   │            │
          │   │   (Docker/Python)   │  │   (Docker)   │            │
          │   │  Semantic Chunking  │  │ Vector Store │            │
          │   └─────────────────────┘  └──────────────┘            │
          │              Docker Services                           │
          └────────────────────────────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────────────────────────┐
│                    Streaming Layer                               │
│              Centrifugo WebSocket (existing)                     │
└─────────────────────────────────────────────────────────────────┘
```

## Why Symfony AI?

[Symfony AI](https://symfony.com/doc/current/ai/bundles/ai-bundle.html) (released January 2026) provides:
- **Unified Platform interface** for OpenAI, Anthropic, Azure, Google, Mistral
- **Built-in Failover** - automatic fallback when primary provider fails
- **Embeddings generation** - used to create vectors for ChromaDB
- **Tool/Function calling** - abstracted across providers
- **YAML configuration** - declarative provider setup

This eliminates the need to build custom LLM abstraction layer.

## Why ChromaDB over pgvector?

- **Dedicated vector database** - optimized for similarity search
- **Built-in embedding functions** - OpenAI, Jina, HuggingFace, Ollama wrappers included
- **Docker-native** - just add to docker-compose
- **PHP SDK** - [codewithkyrian/chromadb-php](https://github.com/CodeWithKyrian/chromadb-php) (used by Symfony)

## Module Structure

```
src/EmployeePortal/Chatbot/
├── Conversation/           # Chat session management
│   ├── Conversation.php    # Aggregate root
│   ├── Message/            # User/assistant messages
│   └── Features/
│       ├── StartConversation/
│       ├── SendMessage/
│       └── GetHistory/
├── Rag/                    # Knowledge retrieval
│   ├── Document/           # Indexed content entities
│   ├── Indexing/           # Blog post indexer, chunking
│   └── Retrieval/          # Search service using ai-postgres-store
├── Tool/                   # Function calling implementations
│   └── BuiltIn/
│       ├── CreateSupportTicketTool.php
│       ├── LookupUserDataTool.php
│       └── SearchKnowledgeBaseTool.php
└── Support/Bundle/
```

Note: No custom `Llm/` directory needed - Symfony AI handles provider abstraction.

## Key Components

### 1. Symfony AI Platform (LLM Layer)

**YAML Configuration** (`config/packages/ai.yaml`):
```yaml
symfony_ai:
    platform:
        anthropic:
            api_key: '%env(ANTHROPIC_API_KEY)%'
            default_model: claude-sonnet-4-20250514
        openai:
            api_key: '%env(OPENAI_API_KEY)%'
            default_model: gpt-4o

    # Failover: try Anthropic first, fallback to OpenAI
    failover:
        platforms: [anthropic, openai]
```

**Usage in Services:**
```php
use Symfony\AI\Platform\PlatformInterface;
use Symfony\AI\Platform\Message\Message;

final readonly class ChatService
{
    public function __construct(
        private PlatformInterface $platform,
    ) {}

    public function chat(array $messages): Generator
    {
        $response = $this->platform->chat($messages, streaming: true);

        foreach ($response as $chunk) {
            yield $chunk;
        }
    }
}
```

**Tool calling** - Symfony AI abstracts tool definitions across providers

### 2. Chonkie Chunking Service (Docker)

Since Chonkie has no official Docker image, we create a lightweight FastAPI wrapper.

**Directory structure:**
```
docker/chonkie/
├── Dockerfile
├── requirements.txt
└── server.py
```

**Dockerfile:**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

**PHP Client (in Symfony):**
```php
final readonly class ChonkieClient
{
    public function __construct(
        private HttpClientInterface $httpClient,
        #[Autowire('%env(CHONKIE_URL)%')]
        private string $baseUrl = 'http://chonkie:8000',
    ) {}

    /** @return list<array{index: int, content: string, token_count: int}> */
    public function chunk(string $content, string $strategy = 'semantic'): array
    {
        $response = $this->httpClient->request('POST', $this->baseUrl . '/chunk', [
            'json' => [
                'content' => $content,
                'strategy' => $strategy,
                'max_tokens' => 512,
            ],
        ]);

        return $response->toArray()['chunks'];
    }
}
```

### 3. ChromaDB Vector Store (Docker)

**docker-compose.yaml addition:**
```yaml
services:
  chromadb:
    image: chromadb/chroma:latest
    ports:
      - "8002:8000"
    environment:
      - IS_PERSISTENT=TRUE
      - CHROMA_SERVER_AUTH_CREDENTIALS=your-secure-token
      - CHROMA_SERVER_AUTH_TOKEN_TRANSPORT_HEADER=Authorization
    volumes:
      - chromadb_data:/chroma/chroma
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/v2/heartbeat"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  chromadb_data:
```

**PHP SDK installation:**
```bash
composer require codewithkyrian/chromadb-php
```

**ChromaDB Client wrapper:**
```php
use Codewithkyrian\ChromaDB\ChromaDB;
use Codewithkyrian\ChromaDB\Embeddings\OpenAIEmbeddingFunction;
use Codewithkyrian\ChromaDB\Types\Includes;

final readonly class VectorStoreService
{
    private const COLLECTION_NAME = 'blog_chunks';

    private ChromaDB $client;
    private OpenAIEmbeddingFunction $embeddingFunction;

    public function __construct(
        #[Autowire('%env(CHROMADB_HOST)%')]
        string $host,
        #[Autowire('%env(OPENAI_API_KEY)%')]
        string $openaiApiKey,
    ) {
        $this->client = ChromaDB::local()
            ->withHost($host)
            ->withPort(8000)
            ->connect();

        $this->embeddingFunction = new OpenAIEmbeddingFunction($openaiApiKey);
    }

    public function indexChunks(string $documentId, array $chunks): void
    {
        $collection = $this->client->getOrCreateCollection(
            name: self::COLLECTION_NAME,
            embeddingFunction: $this->embeddingFunction,
        );

        $ids = [];
        $documents = [];
        $metadatas = [];

        foreach ($chunks as $i => $chunk) {
            $ids[] = "{$documentId}_{$i}";
            $documents[] = $chunk['content'];
            $metadatas[] = [
                'document_id' => $documentId,
                'chunk_index' => $i,
                'token_count' => $chunk['token_count'],
            ];
        }

        // Embeddings auto-generated by collection's embeddingFunction
        $collection->add(
            ids: $ids,
            documents: $documents,
            metadatas: $metadatas,
        );
    }

    public function search(string $query, int $limit = 5): array
    {
        $collection = $this->client->getCollection(
            name: self::COLLECTION_NAME,
            embeddingFunction: $this->embeddingFunction,
        );

        // Query text auto-embedded by embeddingFunction
        $results = $collection->query(
            queryTexts: [$query],
            nResults: $limit,
        );

        return $results->asRecords();
    }
}
```

### 4. RAG Indexing Flow

```
Blog Post (HTML)
    → ChonkieClient::chunk()           # Semantic chunks
    → EmbeddingService::embed()        # OpenAI text-embedding-3-small
    → VectorStoreService::indexChunks() # Store in ChromaDB
```

**Embedding provider:** OpenAI `text-embedding-3-small` via Symfony AI Platform

### 3. Streaming via Centrifugo

**Flow:**
1. User sends message via `POST /conversations/{id}/messages`
2. API returns `202 Accepted` with `stream_id`
3. Backend streams LLM tokens to Centrifugo channel `chat:{conversation_id}#{user_id}`
4. Frontend receives WebSocket events: `chat.stream.start`, `chat.stream.chunk`, `chat.stream.complete`

### 4. Function Calling

**Available tools:**
| Tool | Purpose | Permissions |
|------|---------|-------------|
| `create_support_ticket` | Escalate to human support | ROLE_USER |
| `lookup_user_data` | Query account info, orders | ROLE_USER (own data) |
| `search_knowledge_base` | RAG search | ROLE_USER |

**Security layers:**
- Role-based authorization
- Resource-level checks (users can only access own data)
- Audit logging for all tool executions
- Rate limiting per tool

### 5. Conversation Persistence

**Tables:**
- `chatbot_conversations` - Session metadata, user_id, status
- `chatbot_messages` - Role, content, tool_calls, token_count

**Context window management:**
- Keep recent messages within token limit
- Summarize older messages for long conversations

## API Endpoints

```
POST   /api/example-project/chatbot/conversations           # Start conversation
GET    /api/example-project/chatbot/conversations           # List conversations
GET    /api/example-project/chatbot/conversations/{id}      # Get with messages
POST   /api/example-project/chatbot/conversations/{id}/messages  # Send message
DELETE /api/example-project/chatbot/conversations/{id}      # Archive
```

## Temporal Workflows

Use for long-running operations:
- **DocumentIndexingWorkflow** - Batch chunking, embedding, storage
- **ScheduledReindexingWorkflow** - Periodic RAG index refresh

## Implementation Phases

### Phase 1: Chonkie Servicel
- [ ] Create `ChonkieClient` PHP service
- [ ] Test chunking with sample HTML content

### Phase 3: Streaming
- [ ] Integrate Centrifugo for response streaming
- [ ] Bridge Symfony AI streaming to WebSocket events
- [ ] WebSocket channel authorization

### Phase 4: RAG
- [ ] Add ChromaDB to docker-compose.yaml
- [ ] Install `codewithkyrian/chromadb-php` SDK
- [ ] Create `VectorStoreService` with OpenAI embedding function
- [ ] Blog post indexer using ChonkieClient + ChromaDB
- [ ] Search retrieval service

### Phase 5: Function Calling
- [ ] Define tools using Symfony AI tool abstraction
- [ ] Built-in tools (support ticket, user lookup, KB search)
- [ ] Security/authorization layer
- [ ] Tool execution in chat loop

### Phase 6: Polish
- [ ] Context window management
- [ ] Conversation summarization (long chats)
- [ ] Monitoring, metrics, cost tracking

## Critical Files to Reference

| Purpose | File |
|---------|------|
| Service pattern | `src/EmployeePortal/Blog/Post/Features/Create/Port/CreatePostService.php` |
| Centrifugo integration | `src/Infra/WebSocket/Features/SendEvent/Port/SendEventCommand.php` |
| Temporal workflows | `src/Playground/Temporal/Subscription/Workflow/SubscriptionWorkflow.php` |
| Bundle structure | `src/EmployeePortal/Blog/Support/Bundle/DependencyInjection/AppBlogExtension.php` |
| Security config | `config/packages/security.yaml` |

## Verification Plan

1. **Docker services:**
   ```bash
   # Start all services
   docker-compose up chonkie chromadb -d

   # Test Chonkie health
   curl http://localhost:8001/health

   # Test Chonkie chunking
   curl -X POST http://localhost:8001/chunk \
     -H "Content-Type: application/json" \
     -d '{"content": "<h1>Title</h1><p>Paragraph one.</p><p>Paragraph two.</p>", "strategy": "semantic", "overlap": }'

   # Test ChromaDB health
   curl http://localhost:8002/api/v2/heartbeat
   ```

2. **Integration tests** - Full RAG pipeline (chunk → embed → store → retrieve)
3. **Manual testing:**
   - Start conversation via API
   - Verify streaming via WebSocket client
   - Test function calling (create ticket, lookup data)
   - Verify RAG retrieval relevance

**Sources:**
- [Symfony AI Bundle](https://symfony.com/doc/current/ai/bundles/ai-bundle.html)
- [ChromaDB PHP SDK](https://github.com/CodeWithKyrian/chromadb-php)
- [Chonkie](https://github.com/chonkie-inc/chonkie)