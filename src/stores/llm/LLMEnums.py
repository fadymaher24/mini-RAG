from enum import Enum


class LLMEnum(Enum):
    OPENAI = "OPENAI"
    ANTHROPIC = "ANTHROPIC"
    AZURE_OPENAI = "AZURE_OPENAI"
    COHERE = "COHERE"


class OpenAIEnums(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class CohereEnums(Enum):
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"

    DOCUMENT = "search_document"
    QUERY = "search_query"


class DocumentTypeEnums(Enum):
    DOCUMENT = "document"
    QUERY = "query"
