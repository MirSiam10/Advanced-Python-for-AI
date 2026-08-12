# This function accepts either a string or a list of strings
def process_input(data: str | list[str]) -> list[str]:
    if isinstance(data, str):
        return [data]        # wrap single string in a list
    return data              # already a list


process_input("hello")           #valid
process_input(["hello", "world"]) #valid
process_input(str(42))            # pass a string to satisfy the type hint