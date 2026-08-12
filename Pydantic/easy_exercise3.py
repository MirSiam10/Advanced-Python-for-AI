"""E3. Take your build_messages function from Lesson 1's challenge exercise and rewrite it so it returns list[Message] — using the Message Pydantic model from this lesson."""

from pydantic import BaseModel
from typing import Literal


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


def build_messages(
    system_prompt: str,
    user_messages: list[str]
) -> list[Message]:
    """
    Build a list of Message objects for an LLM conversation.

    Args:
        system_prompt: The system instruction.
        user_messages: A list of user messages.

    Returns:
        A list of Message objects.
    """
    messages = [
        Message(role="system", content=system_prompt)
    ]

    messages.extend(
        Message(role="user", content=message)
        for message in user_messages
    )

    return messages


messages = build_messages(
    system_prompt="You are a helpful assistant.",
    user_messages=[
        "Hello!",
        "Explain Python.",
        "Give an example."
    ]
)

for message in messages:
    print(message.model_dump())