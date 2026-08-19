import asyncio

async def fetch_info_model(model_name : str) ->dict[str, str]:

    print(f"Fetching info for model: {model_name}")
    await asyncio.sleep(1)

    return {"model_name": model_name,
            "Provider" : "OpenAI"}

async def main () -> None:
    model_info = await fetch_info_model("gpt-4")
    print(f"Model info: {model_info}")

asyncio.run(main()) 
    