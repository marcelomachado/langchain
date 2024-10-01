"""
This file contains a mapping between the lc_namespace path for a given
subclass that implements from Serializable to the namespace
where that class is actually located.

This mapping helps maintain the ability to serialize and deserialize
well-known LangChain objects even if they are moved around in the codebase
across different LangChain versions.

For example,

The code for AIMessage class is located in
langchain_core.messages.ai.AIMessage,
This message is associated with the lc_namespace
["langchain", "schema", "messages", "AIMessage"],
because this code was originally in langchain.schema.messages.AIMessage.

The mapping allows us to deserialize an AIMessage created with an older
version of LangChain where the code was in a different location.
"""

# First value is the value that it is serialized as
# Second value is the path to load it from
SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain", "schema", "messages", "AIMessage"): (
        "langchain_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "messages", "AIMessageChunk"): (
        "langchain_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("langchain", "schema", "messages", "BaseMessage"): (
        "langchain_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("langchain", "schema", "messages", "BaseMessageChunk"): (
        "langchain_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessage"): (
        "langchain_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "messages", "FunctionMessage"): (
        "langchain_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "messages", "HumanMessage"): (
        "langchain_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "messages", "SystemMessage"): (
        "langchain_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "messages", "ToolMessage"): (
        "langchain_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("langchain", "schema", "messages", "RemoveMessage"): (
        "langchain_core",
        "messages",
        "modifier",
        "RemoveMessage",
    ),
    ("langchain", "schema", "agent", "AgentAction"): (
        "langchain_core",
        "agents",
        "AgentAction",
    ),
    ("langchain", "schema", "agent", "AgentFinish"): (
        "langchain_core",
        "agents",
        "AgentFinish",
    ),
    ("langchain", "schema", "prompt_template", "BasePromptTemplate"): (
        "langchain_core",
        "prompts",
        "base",
        "BasePromptTemplate",
    ),
    ("langchain", "chains", "llm", "LLMChain"): (
        "langchain",
        "chains",
        "llm",
        "LLMChain",
    ),
    ("langchain", "prompts", "prompt", "PromptTemplate"): (
        "langchain_core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("langchain", "prompts", "chat", "MessagesPlaceholder"): (
        "langchain_core",
        "prompts",
        "chat",
        "MessagesPlaceholder",
    ),
    ("langchain", "llms", "openai", "OpenAI"): (
        "langchain_openai",
        "llms",
        "base",
        "OpenAI",
    ),
    ("langchain", "prompts", "chat", "ChatPromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("langchain", "prompts", "image", "ImagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "schema", "agent", "AgentActionMessageLog"): (
        "langchain_core",
        "agents",
        "AgentActionMessageLog",
    ),
    ("langchain", "schema", "agent", "ToolAgentAction"): (
        "langchain",
        "agents",
        "output_parsers",
        "tools",
        "ToolAgentAction",
    ),
    ("langchain", "prompts", "chat", "BaseMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("langchain", "schema", "output", "ChatGeneration"): (
        "langchain_core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("langchain", "schema", "output", "Generation"): (
        "langchain_core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("langchain", "schema", "document", "Document"): (
        "langchain_core",
        "documents",
        "base",
        "Document",
    ),
    ("langchain", "output_parsers", "fix", "OutputFixingParser"): (
        "langchain",
        "output_parsers",
        "fix",
        "OutputFixingParser",
    ),
    ("langchain", "prompts", "chat", "AIMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "AIMessagePromptTemplate",
    ),
    ("langchain", "output_parsers", "regex", "RegexParser"): (
        "langchain",
        "output_parsers",
        "regex",
        "RegexParser",
    ),
    ("langchain", "schema", "runnable", "DynamicRunnable"): (
        "langchain_core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("langchain", "schema", "prompt", "PromptValue"): (
        "langchain_core",
        "prompt_values",
        "PromptValue",
    ),
    ("langchain", "schema", "runnable", "RunnableBinding"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("langchain", "schema", "runnable", "RunnableBranch"): (
        "langchain_core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("langchain", "schema", "runnable", "RunnableWithFallbacks"): (
        "langchain_core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("langchain", "schema", "output_parser", "StrOutputParser"): (
        "langchain_core",
        "output_parsers",
        "string",
        "StrOutputParser",
    ),
    ("langchain", "chat_models", "openai", "ChatOpenAI"): (
        "langchain_openai",
        "chat_models",
        "base",
        "ChatOpenAI",
    ),
    (
      "langchain",
      "output_parsers",
      "list",
      "CommaSeparatedListOutputParser"
    ): (
        "langchain_core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    (
      "langchain",
      "output_parsers",
      "list",
      "CommaSeparatedNumericListOutputParser"
    ): (
        "langchain_core",
        "output_parsers",
        "list",
        "CommaSeparatedNumericListOutputParser",
    ),
    ("langchain", "schema", "runnable", "RunnableParallel"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableParallel",
    ),
    ("langchain", "chat_models", "azure_openai", "AzureChatOpenAI"): (
        "langchain_openai",
        "chat_models",
        "azure",
        "AzureChatOpenAI",
    ),
    ("langchain", "chat_models", "bedrock", "BedrockChat"): (
        "langchain_aws",
        "chat_models",
        "bedrock",
        "ChatBedrock",
    ),
    ("langchain", "chat_models", "anthropic", "ChatAnthropic"): (
        "langchain_anthropic",
        "chat_models",
        "ChatAnthropic",
    ),
    ("langchain_groq", "chat_models", "ChatGroq"): (
        "langchain_groq",
        "chat_models",
        "ChatGroq",
    ),
    ("langchain", "chat_models", "fireworks", "ChatFireworks"): (
        "langchain_fireworks",
        "chat_models",
        "ChatFireworks",
    ),
    ("langchain", "chat_models", "google_palm", "ChatGooglePalm"): (
        "langchain",
        "chat_models",
        "google_palm",
        "ChatGooglePalm",
    ),
    ("langchain", "chat_models", "vertexai", "ChatVertexAI"): (
        "langchain_google_vertexai",
        "chat_models",
        "ChatVertexAI",
    ),
    ("langchain", "chat_models", "mistralai", "ChatMistralAI"): (
        "langchain_mistralai",
        "chat_models",
        "ChatMistralAI",
    ),
    ("langchain", "chat_models", "bedrock", "ChatBedrock"): (
        "langchain_aws",
        "chat_models",
        "bedrock",
        "ChatBedrock",
    ),
    ("langchain_google_genai", "chat_models", "ChatGoogleGenerativeAI"): (
        "langchain_google_genai",
        "chat_models",
        "ChatGoogleGenerativeAI",
    ),
    ("langchain", "schema", "output", "ChatGenerationChunk"): (
        "langchain_core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessageChunk"): (
        "langchain_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("langchain", "schema", "messages", "HumanMessageChunk"): (
        "langchain_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("langchain", "schema", "messages", "FunctionMessageChunk"): (
        "langchain_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("langchain", "schema", "messages", "SystemMessageChunk"): (
        "langchain_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("langchain", "schema", "messages", "ToolMessageChunk"): (
        "langchain_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("langchain", "schema", "output", "GenerationChunk"): (
        "langchain_core",
        "outputs",
        "generation",
        "GenerationChunk",
    ),
    ("langchain", "llms", "openai", "BaseOpenAI"): (
        "langchain",
        "llms",
        "openai",
        "BaseOpenAI",
    ),
    ("langchain", "llms", "bedrock", "Bedrock"): (
        "langchain_aws",
        "llms",
        "bedrock",
        "BedrockLLM",
    ),
    ("langchain", "llms", "fireworks", "Fireworks"): (
        "langchain_fireworks",
        "llms",
        "Fireworks",
    ),
    ("langchain", "llms", "google_palm", "GooglePalm"): (
        "langchain",
        "llms",
        "google_palm",
        "GooglePalm",
    ),
    ("langchain", "llms", "openai", "AzureOpenAI"): (
        "langchain_openai",
        "llms",
        "azure",
        "AzureOpenAI",
    ),
    ("langchain", "llms", "replicate", "Replicate"): (
        "langchain",
        "llms",
        "replicate",
        "Replicate",
    ),
    ("langchain", "llms", "vertexai", "VertexAI"): (
        "langchain_vertexai",
        "llms",
        "VertexAI",
    ),
    ("langchain", "output_parsers", "combining", "CombiningOutputParser"): (
        "langchain",
        "output_parsers",
        "combining",
        "CombiningOutputParser",
    ),
    ("langchain", "schema", "prompt_template", "BaseChatPromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    (
      "langchain",
      "prompts",
      "few_shot_with_templates",
      "FewShotPromptWithTemplates"
    ): (
        "langchain_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("langchain", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "langchain_core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptTemplate"): (
        "langchain_core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptValue"): (
        "langchain_core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("langchain", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValue"): (
        "langchain_core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValueConcrete"): (
        "langchain_core",
        "prompt_values",
        "ChatPromptValueConcrete",
    ),
    ("langchain", "schema", "runnable", "HubRunnable"): (
        "langchain",
        "runnables",
        "hub",
        "HubRunnable",
    ),
    ("langchain", "schema", "runnable", "RunnableBindingBase"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableBindingBase",
    ),
    ("langchain", "schema", "runnable", "OpenAIFunctionsRouter"): (
        "langchain",
        "runnables",
        "openai_functions",
        "OpenAIFunctionsRouter",
    ),
    ("langchain", "schema", "runnable", "RouterRunnable"): (
        "langchain_core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("langchain", "schema", "runnable", "RunnablePassthrough"): (
        "langchain_core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("langchain", "schema", "runnable", "RunnableSequence"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("langchain", "schema", "runnable", "RunnableEach"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("langchain", "schema", "runnable", "RunnableEachBase"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableAlternatives"): (
        "langchain_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableFields"): (
        "langchain_core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("langchain", "schema", "runnable", "RunnableWithMessageHistory"): (
        "langchain_core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("langchain", "schema", "runnable", "RunnableAssign"): (
        "langchain_core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("langchain", "schema", "runnable", "RunnableRetry"): (
        "langchain_core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
    ("langchain_core", "prompts", "structured", "StructuredPrompt"): (
        "langchain_core",
        "prompts",
        "structured",
        "StructuredPrompt",
    ),
}

# Needed for backwards compatibility for old versions of LangChain where things
# Were in different place
_OG_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain", "schema", "AIMessage"): (
        "langchain_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "ChatMessage"): (
        "langchain_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "FunctionMessage"): (
        "langchain_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "HumanMessage"): (
        "langchain_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "SystemMessage"): (
        "langchain_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "prompt_template", "ImagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "schema", "agent", "OpenAIToolAgentAction"): (
        "langchain",
        "agents",
        "output_parsers",
        "openai_tools",
        "OpenAIToolAgentAction",
    ),
}

# Needed for backwards compatibility for a few versions where we serialized
# with langchain_core paths.
OLD_CORE_NAMESPACES_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain_core", "messages", "ai", "AIMessage"): (
        "langchain_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain_core", "messages", "ai", "AIMessageChunk"): (
        "langchain_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("langchain_core", "messages", "base", "BaseMessage"): (
        "langchain_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("langchain_core", "messages", "base", "BaseMessageChunk"): (
        "langchain_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("langchain_core", "messages", "chat", "ChatMessage"): (
        "langchain_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain_core", "messages", "function", "FunctionMessage"): (
        "langchain_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain_core", "messages", "human", "HumanMessage"): (
        "langchain_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain_core", "messages", "system", "SystemMessage"): (
        "langchain_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain_core", "messages", "tool", "ToolMessage"): (
        "langchain_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("langchain_core", "agents", "AgentAction"): (
        "langchain_core",
        "agents",
        "AgentAction",
    ),
    ("langchain_core", "agents", "AgentFinish"): (
        "langchain_core",
        "agents",
        "AgentFinish",
    ),
    ("langchain_core", "prompts", "base", "BasePromptTemplate"): (
        "langchain_core",
        "prompts",
        "base",
        "BasePromptTemplate",
    ),
    ("langchain_core", "prompts", "prompt", "PromptTemplate"): (
        "langchain_core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("langchain_core", "prompts", "chat", "MessagesPlaceholder"): (
        "langchain_core",
        "prompts",
        "chat",
        "MessagesPlaceholder",
    ),
    ("langchain_core", "prompts", "chat", "ChatPromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("langchain_core", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("langchain_core", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("langchain_core", "agents", "AgentActionMessageLog"): (
        "langchain_core",
        "agents",
        "AgentActionMessageLog",
    ),
    ("langchain_core", "prompts", "chat", "BaseMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("langchain_core", "outputs", "chat_generation", "ChatGeneration"): (
        "langchain_core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("langchain_core", "outputs", "generation", "Generation"): (
        "langchain_core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("langchain_core", "documents", "base", "Document"): (
        "langchain_core",
        "documents",
        "base",
        "Document",
    ),
    ("langchain_core", "prompts", "chat", "AIMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "AIMessagePromptTemplate",
    ),
    ("langchain_core", "runnables", "configurable", "DynamicRunnable"): (
        "langchain_core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("langchain_core", "prompt_values", "PromptValue"): (
        "langchain_core",
        "prompt_values",
        "PromptValue",
    ),
    ("langchain_core", "runnables", "base", "RunnableBinding"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("langchain_core", "runnables", "branch", "RunnableBranch"): (
        "langchain_core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("langchain_core", "runnables", "fallbacks", "RunnableWithFallbacks"): (
        "langchain_core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("langchain_core", "output_parsers", "string", "StrOutputParser"): (
        "langchain_core",
        "output_parsers",
        "string",
        "StrOutputParser",
    ),
    (
      "langchain_core",
      "output_parsers",
      "list",
      "CommaSeparatedListOutputParser"
    ): (
        "langchain_core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    (
      "langchain_core",
      "output_parsers",
      "list",
      "CommaSeparatedNumericListOutputParser"
    ): (
        "langchain_core",
        "output_parsers",
        "list",
        "CommaSeparatedNumericListOutputParser",
    ),
    ("langchain_core", "runnables", "base", "RunnableParallel"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableParallel",
    ),
    ("langchain_core", "outputs", "chat_generation", "ChatGenerationChunk"): (
        "langchain_core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("langchain_core", "messages", "chat", "ChatMessageChunk"): (
        "langchain_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("langchain_core", "messages", "human", "HumanMessageChunk"): (
        "langchain_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("langchain_core", "messages", "function", "FunctionMessageChunk"): (
        "langchain_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("langchain_core", "messages", "system", "SystemMessageChunk"): (
        "langchain_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("langchain_core", "messages", "tool", "ToolMessageChunk"): (
        "langchain_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("langchain_core", "outputs", "generation", "GenerationChunk"): (
        "langchain_core",
        "outputs",
        "generation",
        "GenerationChunk",
    ),
    ("langchain_core", "prompts", "chat", "BaseChatPromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("langchain_core", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    (
        "langchain_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ): (
        "langchain_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("langchain_core", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "langchain_core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("langchain_core", "prompts", "string", "StringPromptTemplate"): (
        "langchain_core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("langchain_core", "prompt_values", "StringPromptValue"): (
        "langchain_core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("langchain_core", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("langchain_core", "prompt_values", "ChatPromptValue"): (
        "langchain_core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("langchain_core", "prompt_values", "ChatPromptValueConcrete"): (
        "langchain_core",
        "prompt_values",
        "ChatPromptValueConcrete",
    ),
    ("langchain_core", "runnables", "base", "RunnableBindingBase"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableBindingBase",
    ),
    ("langchain_core", "runnables", "router", "RouterRunnable"): (
        "langchain_core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("langchain_core", "runnables", "passthrough", "RunnablePassthrough"): (
        "langchain_core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("langchain_core", "runnables", "base", "RunnableSequence"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("langchain_core", "runnables", "base", "RunnableEach"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("langchain_core", "runnables", "base", "RunnableEachBase"): (
        "langchain_core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    (
        "langchain_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ): (
        "langchain_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    (
      "langchain_core",
      "runnables",
      "configurable",
      "RunnableConfigurableFields"
    ): (
        "langchain_core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("langchain_core", "runnables", "history", "RunnableWithMessageHistory"): (
        "langchain_core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("langchain_core", "runnables", "passthrough", "RunnableAssign"): (
        "langchain_core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("langchain_core", "runnables", "retry", "RunnableRetry"): (
        "langchain_core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
}

_JS_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain_core", "messages", "AIMessage"): (
        "langchain_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain_core", "messages", "AIMessageChunk"): (
        "langchain_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("langchain_core", "messages", "BaseMessage"): (
        "langchain_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("langchain_core", "messages", "BaseMessageChunk"): (
        "langchain_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("langchain_core", "messages", "ChatMessage"): (
        "langchain_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain_core", "messages", "ChatMessageChunk"): (
        "langchain_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("langchain_core", "messages", "FunctionMessage"): (
        "langchain_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain_core", "messages", "FunctionMessageChunk"): (
        "langchain_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("langchain_core", "messages", "HumanMessage"): (
        "langchain_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain_core", "messages", "HumanMessageChunk"): (
        "langchain_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("langchain_core", "messages", "SystemMessage"): (
        "langchain_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain_core", "messages", "SystemMessageChunk"): (
        "langchain_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("langchain_core", "messages", "ToolMessage"): (
        "langchain_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("langchain_core", "messages", "ToolMessageChunk"): (
        "langchain_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("langchain_core", "prompts", "image", "ImagePromptTemplate"): (
        "langchain_core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "chat_models", "bedrock", "ChatBedrock"): (
        "langchain_aws",
        "chat_models",
        "ChatBedrock",
    ),
    ("langchain", "chat_models", "google_genai", "ChatGoogleGenerativeAI"): (
        "langchain_google_genai",
        "chat_models",
        "ChatGoogleGenerativeAI",
    ),
    ("langchain", "chat_models", "groq", "ChatGroq"): (
        "langchain_groq",
        "chat_models",
        "ChatGroq",
    ),
    ("langchain", "chat_models", "bedrock", "BedrockChat"): (
        "langchain_aws",
        "chat_models",
        "ChatBedrock",
    ),
}
