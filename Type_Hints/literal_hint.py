from typing import Literal


def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    print(f"Log level set to: {level}")


set_log_level("DEBUG")    # ✅
set_log_level("INFO")     # ✅
#set_log_level("VERBOSE")  # ❌ type checker catches this immediately