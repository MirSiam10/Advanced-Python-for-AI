'''Optional — "This or None"

Optional[X] is exactly the same as X | None. It's older syntax but you'll see it everywhere in existing codebases: '''


from typing import Optional

# These two are identical:
def find_user_union(user_id: int) -> str | None:
    ...

def find_user(user_id: int) -> Optional[str]:
    ...

#Use X | None in new code. Use Optional[X] when reading older code. Know both.