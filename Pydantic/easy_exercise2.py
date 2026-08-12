"""E2. Create a Pydantic model called AgentConfig with fields: name (str), max_iterations (int, default 10, must be > 0), verbose (bool, default False), tools (list of strings, default empty list). Test it with valid and invalid data."""

from pydantic import BaseModel, Field, ValidationError


class AgentConfig(BaseModel):
    name: str
    max_iterations: int = Field(default=10, gt=0)
    verbose: bool = False
    tools: list[str] = []


# Valid data
config = AgentConfig(
    name="Research Agent",
    max_iterations=20,
    verbose=True,
    tools=["search", "calculator"]
)

print("Valid config:")
print(config.model_dump())


print("\nInvalid config:")

try:
    bad_config = AgentConfig(
        name="Broken Agent",
        max_iterations=0
    )
except ValidationError as e:
    print(e)