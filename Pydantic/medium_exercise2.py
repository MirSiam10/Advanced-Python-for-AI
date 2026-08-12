#M2. Create a ChatRequest model (like in the walkthrough, but your own version). Add a custom field_validator that ensures no message's content is longer than 4000 characters. Test it with both valid and invalid input.


from typing import Literal

from pydantic import BaseModel, ValidationError, field_validator


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    model: str = "gpt-5.5"
    temperature: float = 0.7
    messages: list[Message]

    @field_validator("messages")
    @classmethod
    def validate_message_length(cls, messages: list[Message]):
        for message in messages:
            if len(message.content) > 4000:
                raise ValueError(
                    f"Message from '{message.role}' exceeds 4000 characters."
                )
        return messages


# ----------------------------
# Valid Example
# ----------------------------

valid_request = ChatRequest(
    messages=[
        Message(
            role="system",
            content="You are a helpful assistant."
        ),
        Message(
            role="user",
            content="Explain decorators in Python."
        ),
    ]
)

print("Valid Request:")
print(valid_request.model_dump())


# ----------------------------
# Invalid Example
# ----------------------------

try:
    invalid_request = ChatRequest(
        messages=[
            Message(
                role="user",
                content="A" * 4001
            )
        ]
    )

except ValidationError as e:
    print("\nValidation Error:")
    print(e)