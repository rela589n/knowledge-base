---
aliases:
  - RAG
---
**RAG** - lets an LLM answer questions regarding your data.
	Search first - then answer.

- AI answers based on *your* docs, not just training data
- No need to fine-tune a model
- Data can be updated without retraining

## The Problem

LLMs know nothing about your website and documents.

They can only answer from their training data.

## The Solution

Before asking the AI, search your own documents first, 
give that context to the AI along with the question.

### Smart Assistant

It's like a smart assistant who knows nothing about your company.
Instead of memorizing everything, he has a search tool.

When a customer asks something, the assistant:
1. Searches your files for relevant info
2. Reads what they found
3. Answers the customer using that info

### Example

Without RAG:
> User: "How much does your Pro plan cost?"
> AI: "I don't have that information."

With RAG:
> User: "How much does your Pro plan cost?"
> *System finds pricing.md → passes it to AI*
> AI: "The Pro plan costs $29/month and includes..."

## Retrieval Augmented Generation

1. Find relevant [[Chunk|Chunks]] (using [[Vector DB]]);
2. Inject them into a prompt;
   <u>TEXT CHUNKS</u> are fed into LLM, not vectors.
3. Let LLM generate the answer.
