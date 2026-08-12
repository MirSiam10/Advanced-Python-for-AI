from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: list[Message]
    temperature: float = 0.7
    max_tokens: int = 1000


# Pydantic validates the entire nested structure
request = ChatRequest(
    model="gpt-4o",
    messages=[
        Message(role="system", content="You are a helpful assistant."),
        Message(role="user", content="What is RAG?"),
    ],
)

# Each item in messages is now a proper Message object
print(type(request.messages[0]))          # <class 'Message'>
print(request.messages[0].role)           # "system"
print(request.messages[1].content)        # "What is RAG?"