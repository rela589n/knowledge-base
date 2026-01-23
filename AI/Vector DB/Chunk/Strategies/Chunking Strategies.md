**Semantic Chunking** — splits text based on meaning/topic shifts
	Uses embeddings to detect when content changes topic
	Pros
		Preserves context within each chunk
		Better retrieval quality for conceptual queries
	Cons
		More computationally expensive
		Requires embedding model during chunking

**Recursive Chunking** — splits hierarchically using separators (paragraphs → sentences → words)
	Falls back to smaller separators when chunks exceed size limit
	Pros
		Fast and deterministic
		No ML models needed
		Works well for structured documents
	Cons
		May cut mid-thought
		Chunk boundaries are syntactic, not semantic

**When to use which**
	Semantic
		Unstructured text (articles, conversations)
		Quality-critical RAG pipelines
	Recursive
		Code, markdown, structured docs
		Large-scale ingestion where speed matters
		When documents already have clear structure
