---
aliases:
  - document processor
  - document processors
  - processing chain
---
**Document Processing** — a framework for transforming documents in the [[Container Cluster]]
	before they reach the [[Content Cluster]].

## Feed Path

```
Client
   │
   ▼
Container
   ├── document-api (receives HTTP request)
   ├── document-processing (runs processors)
   │
   └──► forwards to ──►  Content Node
                              │
                              ▼
                          Indexing
```

Processing happens inline at the container
	— no roundtrip to content nodes.

> [!tip] Key Insight
> Documents are processed in the container **before** reaching content nodes.
> The `<document-processing cluster="...">` in content config is a routing declaration,
> 	not a "send back" instruction.

---

## Why Use It

Transform documents at ingestion time:
- Field enrichment (add timestamps, compute values)
- Embedding generation (call external ML service)
- Language detection
- HTML removal / text extraction
- Validation / rejection of bad documents
- Character set transcoding

Key benefit: code deploys atomically with your Vespa app
	→ no separate ETL pipeline to manage.

---

## Document Processors

A Java class extending `DocumentProcessor`
	that implements `process()` method.

```java
public class MyProcessor extends DocumentProcessor {
    @Override
    public Progress process(Processing processing) {
        for (DocumentOperation op : processing.getDocumentOperations()) {
            if (op instanceof DocumentPut put) {
                Document doc = put.getDocument();
                doc.setFieldValue("processed", true);
            }
        }
        return Progress.DONE;
    }
}
```

There might be some built-in processors you can use.

## Processing Chains

Ordered list of processors executed sequentially.

```xml
<container id="default" version="1.0">
    <document-processing>
        <chain id="my-chain">
            <documentprocessor id="ai.MyValidator" />
            <documentprocessor id="ai.MyEnricher" />
            <documentprocessor id="ai.MyEmbedder" />
        </chain>
    </document-processing>
</container>
```

Multiple chains can coexist for different purposes.

---

## Configuration

### Enable in Container

```xml
<container id="default" version="1.0">
    <document-api />
    <document-processing /> <!-- enables the framework -->
</container>
```

### Link Content Cluster

```xml
<content id="my-content" version="1.0">
    <documents>
        <document-processing cluster="default" />
    </documents>
</content>
```

This tells Vespa: "documents for this content cluster
	must go through the `default` container's processing chain."

---

## When to Omit

`<document-processing />` is **optional scaffolding**.

If content cluster doesn't reference a processing cluster,
	you can safely omit it.

---

## See Also

- [[services.xml Overview]]
- [[Container Cluster]]
- [[Content Cluster]]
