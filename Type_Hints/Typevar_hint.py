'''TypeVar — Generic Functions

What if you want to write a function that works with any type, but still preserves type information?'''

from typing import TypeVar

T = TypeVar("T")   # T is a placeholder for "any type"


def first_item(items: list[T]) -> T:
    return items[0]


# The return type matches the input type automatically
result_str: str = first_item(["a", "b", "c"])      # T = str
result_int: int = first_item([10, 20, 30])          # T = int
result_float: float = first_item([1.1, 2.2, 3.3])  # T = float


'''
Without TypeVar, you'd have to write Any, losing all type information. With TypeVar, the type checker knows: "whatever type goes in, the same type comes out."

Analogy: Think of T like a variable, but for types instead of values.
'''