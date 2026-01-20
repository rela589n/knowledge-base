
**Goal**: Build an AI-powered support agent using Symfony AI that can answer visitor questions about your website/product.

**Core Requirements**:
- Chat interface for users to ask questions
- Context-aware responses based on your documentation/FAQ
- Conversation history (multi-turn dialogue)
- Fallback to human support when AI can't help

**Tech Stack**:
- Symfony AI Bundle (Platform + Agent + Chat components)
- Vector store for RAG (retrieval from your docs)
- Any LLM provider (OpenAI, Anthropic, or local Ollama)

**Features to Consider**:
- Streaming responses for better UX
- Structured output for ticket creation
- Tool calling (e.g., check order status, search knowledge base)
- Admin panel to review conversations

**Resources**:
- [Symfony AI Documentation](https://symfony.com/doc/current/ai/index.html)
