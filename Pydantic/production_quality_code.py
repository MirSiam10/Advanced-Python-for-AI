



from pydantic import BaseModel, Field, field_validator
from typing import Literal


# Type aliases using Pydantic-friendly patterns
Role = Literal["system", "user", "assistant"]
ModelName = Literal["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"]


class Message(BaseModel):
    """A single message in a conversation."""
    role: Role
    content: str = Field(min_length=1, description="Message content")


class ChatRequest(BaseModel):
    """
    A validated request to the OpenAI Chat Completions API.
    Mirrors the actual API structure with validation.
    """
    model: ModelName = "gpt-4o"
    messages: list[Message] = Field(
        min_length=1,
        description="Conversation history. Must have at least one message.",
    )
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1000, gt=0, le=128000)
    stream: bool = False
    system_prompt: str | None = None

    @field_validator("messages")
    @classmethod
    def last_message_must_be_user(cls, messages: list[Message]) -> list[Message]:
        if messages[-1].role != "user":
            raise ValueError("The last message must have role='user'")
        return messages


class ChatResponse(BaseModel):
    """Parsed response from the OpenAI API."""
    content: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


# Build and validate a request
request = ChatRequest(
    messages=[
        Message(role="system", content="You are a helpful AI assistant."),
        Message(role="user", content="What is a vector database?"),
    ]
)

print(request.model_dump())