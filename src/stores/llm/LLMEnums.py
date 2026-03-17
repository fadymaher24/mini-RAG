from enum import Enum


class LLMEnum(str, Enum):
    OPENAI = "OPENAI"
    ANTHROPIC = "ANTHROPIC"
    AZURE_OPENAI = "AZURE_OPENAI"
    COHERE = "COHERE"


class OpenAIEnums(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
