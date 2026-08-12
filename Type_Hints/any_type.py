from typing import Any

def log_to_console(value: Any) -> None:
    print(f"[LOG] {value}")


log_to_console(42)          # ✅
log_to_console("hello")     # ✅
log_to_console([1, 2, 3])   # ✅
log_to_console(None)        # ✅



'''
When to use it: When genuinely working with data whose type is unknown — like raw JSON from an API, or a generic cache that stores anything.

When NOT to use it: As a lazy shortcut to avoid writing proper types. Overuse of Any defeats the entire purpose of type hints.
'''