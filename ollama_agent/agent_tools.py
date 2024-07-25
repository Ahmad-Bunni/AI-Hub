from langchain_core.tools import tool


@tool()
def weather_forecast(location: str) -> str:
    """Use this tool to get weather forecast information for a given location."""
    return f"{location} is going to be around 43 degrees sunny."


@tool()
def generate_cat_name():
    """Use this tool to generate a cat name"""
    return "Memeow"


tools = [weather_forecast, generate_cat_name]
