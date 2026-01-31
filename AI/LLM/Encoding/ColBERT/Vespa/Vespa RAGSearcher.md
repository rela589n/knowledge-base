How Vespa Implements RAG  
  
Three-step orchestration via RAGSearcher:  
  
```  
User Query → [1. Retrieve Docs] → [2. Build Context] → [3. Prompt LLM] → Answer  
                   ↓                      ↓                    ↓  
              Vespa search         Format as text         OpenAI/etc.  
```  
  
Configuration in services.xml:  
```xml  
<component id="openai" class="ai.vespa.llm.clients.OpenAI">  
    <!-- API key config -->  
</component>  
  
<search>  
    <chain id="rag" inherits="vespa">  
        <searcher id="ai.vespa.search.llm.RAGSearcher">  
            <config name="ai.vespa.search.llm.llm-searcher">  
                <providerId>openai</providerId>  
            </config>  
        </searcher>  
    </chain>  
</search>  
```  
  
Invoking RAG:  
  
```shell  
vespa query \  
  --header="X-LLM-API-KEY:..." \  
  yql="select title,body from docs where userQuery()" \  
  query="what was the manhattan project?" \  
  searchChain=rag  
```