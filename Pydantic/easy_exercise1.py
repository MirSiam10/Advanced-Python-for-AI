"""E1. Create a Pydantic model called EmbeddingRequest with fields: input (str, required, min length 1) and model (str, default "text-embedding-3-small"). Instantiate it with valid data and print .model_dump()."""

from pydantic import BaseModel, Field


class EmbeddingRequest(BaseModel):
    input: str = Field(..., min_length=1)
    model: str = "text-embedding-3-small"


request = EmbeddingRequest(
    input="Hello, OpenAI!"
)

print(request.model_dump())