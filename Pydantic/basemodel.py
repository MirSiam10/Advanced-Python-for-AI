from pydantic import BaseModel


class LLMConfig(BaseModel):
    model: str = "gpt-4o"           # default model
    temperature: float = 0.7        # default temperature
    max_tokens: int = 1000          # default tokens
    stream: bool = False            # default no streaming
    system_prompt: str | None = None  # optional, defaults to None


# Use all defaults
config = LLMConfig()
print(config.model)          # "gpt-4o"
print(config.system_prompt)  # None

# Override some
config = LLMConfig(temperature=0.2, max_tokens=500)
print(config.temperature)    # 0.2
print(config.model)          # "gpt-4o"  ← still the default