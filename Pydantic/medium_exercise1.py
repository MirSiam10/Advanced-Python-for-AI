"""M1. Create two nested Pydantic models: ToolCall (with fields name: str and arguments: dict[str, str]) and AgentStep (with fields thought: str, tool_call: ToolCall | None, and observation: str | None). Instantiate an AgentStep that has a tool call, and one that doesn't. Print both."""

from pydantic import BaseModel


class ToolCall(BaseModel):
    name: str
    arguments: dict[str, str]


class AgentStep(BaseModel):
    thought: str
    tool_call: ToolCall | None = None
    observation: str | None = None


# Agent step with a tool call
step1 = AgentStep(
    thought="I should search for today's weather.",
    tool_call=ToolCall(
        name="weather_search",
        arguments={
            "city": "Dhaka",
            "unit": "celsius"
        }
    ),
    observation="Weather data retrieved successfully."
)

# Agent step without a tool call
step2 = AgentStep(
    thought="I already have enough information.",
    observation="Answer generated."
)

print("Step 1:")
print(step1.model_dump())

print("\nStep 2:")
print(step2.model_dump())