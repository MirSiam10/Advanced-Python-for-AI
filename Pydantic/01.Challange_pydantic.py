import re
from pydantic import BaseModel, Field, ValidationError, field_validator


class LLMConfig(BaseModel):
    model:str
    temperature: float = Field(default = 0.7,  ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, gt = 0)

class PipelineConfig(BaseModel):
    pipeline_name: str
    version: str = Field(default="1.0.0", pattern=r"^\d+\.\d+\.\d+$")
    llmconfig: LLMConfig
    max_retries: int = Field(default=3, ge=0, le=10)
    timeout_seconds: float = Field(default=30.0, gt=0.0)
    tags: list[str] = Field(default_factory=list)

    @field_validator("pipeline_name")
    @classmethod
    def validate_pipeline_name(cls, value: str) -> str:
        if not re.fullmatch(r"[A-Za-z0-9_]+", value):
            raise ValueError(
                "pipeline_name may contain only letters, numbers, and underscores."
            )
        return value

# Valid Configuration

config = PipelineConfig(
    pipeline_name="my_pipeline_1",
    version="1.0.0",
    llmconfig=LLMConfig(
        model="gpt-4o",
        temperature=0.7,
        max_tokens=1024
    ),
    max_retries=3,
    timeout_seconds=30.0,
    tags=["support", "production", "llm"]

)

print("Valid Configuration:")
print(config.model_dump())

try:
    PipelineConfig(
        pipeline_name="Customer Support!",
        llmconfig=LLMConfig(
            model="gpt-5.5",
            temperature=0.3,
            max_tokens=2048
        )
    )
except ValidationError as e:
    print("\nError 1: Invalid pipeline name")
    print(e)

try:
    PipelineConfig(
        pipeline_name="CustomerSupportPipeline",
        version="2.1",
        llmconfig=LLMConfig(
            model="gpt-5.5",
            temperature=0.3,
            max_tokens=2048
        )
    )
except ValidationError as e:
    print("\nError 2: Invalid version")
    print(e)

try:
    PipelineConfig(
        pipeline_name="CustomerSupportPipeline",
        llmconfig=LLMConfig(
            model="gpt-5.5",
            temperature=0.3,
            max_tokens=2048
        ),
        max_retries=20
    )
except ValidationError as e:
    print("\nError 3: Invalid max_retries")
    print(e)
