
#When you receive data from an API or a file, parse it into a Pydantic model:
from pydantic import BaseModel

class EmbeddingResponse(BaseModel):
    object: str
    model: str
    usage: dict[str, int]


# Simulate raw API response (came in as a dict)
raw_response = {
    "object": "list",
    "model": "text-embedding-3-small",
    "usage": {"prompt_tokens": 8, "total_tokens": 8},
}

# Parse and validate
response = EmbeddingResponse.model_validate(raw_response)
print(response.model)                  # "text-embedding-3-small"
print(response.usage["total_tokens"]) # 8