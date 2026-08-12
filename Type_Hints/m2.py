#Medium Exercise 2: Write a function that takes a model name as input and returns a dictionary containing the model's name, maximum token limit, and provider. Use type hints to specify the input and output types.

def get_model_info(model_name: str) -> dict[str, str | int]:
    """
    Return basic information about an AI model.

    Args:
        model_name: The name of the model.

    Returns:
        A dictionary containing the model's name, maximum token limit,
        and provider.
    """
    models: dict[str, dict[str, str | int]] = {
        "gpt-5.5": {
            "name": "gpt-5.5",
            "max_tokens": 128000,
            "provider": "OpenAI",
        },
        "claude-4": {
            "name": "claude-4",
            "max_tokens": 200000,
            "provider": "Anthropic",
        },
        "gemini-2.5": {
            "name": "gemini-2.5",
            "max_tokens": 1000000,
            "provider": "Google",
        },
    }

    return models.get(
        model_name,
        {
            "name": model_name,
            "max_tokens": 0,
            "provider": "Unknown",
        },
    )


def build_messages(system_prompt: str, user_messages: list[str]) -> list[dict[str, str]]:
    """
    Build a list of message dicts including a system prompt and user messages.
    """
    messages: list[dict[str, str]] = []
    messages.append({"role": "system", "content": system_prompt})
    for um in user_messages:
        messages.append({"role": "user", "content": um})
    return messages


system_prompt = "You are a helpful assistant."

user_messages = [
    "Hello!",
    "What is Python?",
    "Give me an example.",
]

messages = build_messages(system_prompt, user_messages)

print(messages)