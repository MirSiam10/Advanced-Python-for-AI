#Easy Exercise 2: Write a function that takes a string and an integer as input and returns a formatted string. Use type hints to specify the input and output types.

def format_prompt(topic: str, max_words: int) -> str:
    
    return f"Please write a detailed explanation about {topic} in no more than {max_words} words."