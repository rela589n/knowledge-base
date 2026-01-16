---
aliases:
  - Jailbreaking
---
Protect from prompt injection ([article](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)).

**Prompt Injection** - users craft prompts to exploit model vulnerabilities to generate inappropriate content.

### Mitigation Strategies

1. **Pre-screening** - Use a lightweight model (e.g., Haiku) to pre-screen user inputs for harmful content before processing

2. **Ethical response Prompt** - Craft prompt for ethical/legal boundaries with explicit refusal instructions

3. **User management** - Throttle or ban users who repeatedly attempt to circumvent guardrails

4. **Monitoring** - Analyze logs for jailbreaking; iteratively refine prompts and validation

> Claude is more resistant to jailbreaking than other major LLMs due to Constitutional AI training.
