# System Architecture

## Components
- **LLM Layer**: Claude 3.5 Sonnet
- **Prompt Layer**: System + Task-specific prompts
- **Tool Layer**: Knowledge base lookup
- **Evaluation Layer**: Automated testing and scoring

## Flow
1. User sends message
2. Agent classifies intent
3. Agent retrieves relevant knowledge
4. Agent generates response
5. Response is evaluated before sending
