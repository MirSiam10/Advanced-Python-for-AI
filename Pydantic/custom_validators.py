#Sometimes you need logic that Field constraints can't express:

from pydantic import BaseModel, Field, field_validator

class ChatRequest(BaseModel):
    model: str
    messages: list[dict]
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)

    @field_validator("model")
    @classmethod
    def validate_model(cls, value: str) -> str:
        allowed = {"gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"}
        if value not in allowed:
            raise ValueError(f"Model must be one of {allowed}, got '{value}'")
        return value

    @field_validator("messages")
    @classmethod
    def validate_messages_not_empty(cls, value: list) -> list:
        if len(value) == 0:
            raise ValueError("messages cannot be empty")
        return value


# ✅ Valid
req = ChatRequest(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
)

# ❌ Invalid model name
req = ChatRequest(
    model="gpt-5-turbo-ultra",
    messages=[{"role": "user", "content": "Hello"}],
)
# ValidationError: model
#   Value error: Model must be one of {'gpt-4o', ...}, got 'gpt-5-turbo-ultra'