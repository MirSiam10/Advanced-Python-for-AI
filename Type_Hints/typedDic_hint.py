# M2
from typing import TypedDict, Literal


class ModelConfig(TypedDict):
    """Configuration for an AI model."""
    model: Literal[
        "gpt-5.5",
        "gpt-4.1",
        "text-embedding-3-small",
    ]
    temperature: float
    max_tokens: int
    stream: bool


def print_model_config(config: ModelConfig) -> None:
    """
    Print a formatted summary of a model configuration.

    Args:
        config: A ModelConfig dictionary.
    """
    print("=== Model Configuration ===")
    print(f"Model       : {config['model']}")
    print(f"Temperature : {config['temperature']}")
    print(f"Max Tokens  : {config['max_tokens']}")
    print(f"Stream      : {config['stream']}")


# Example usage
config: ModelConfig = {
    "model": "gpt-5.5",
    "temperature": 0.7,
    "max_tokens": 1024,
    "stream": True,
}

print_model_config(config)