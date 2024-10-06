from langgraph.prebuilt import ToolNode


def weather_forecast(location: str) -> str:
    """This function provides the weather forecast.

    Args:
        location: (str) weather forecast location.
    """
    return f"The weather in {location} is 36 degrees sunny."


def get_the_time(location: str) -> str:
    """This tool provides the time for a given location.

    Args:
    location: (str) the location to get the time.
    """
    return f"Response: The time in {location} is 6pm."


tools = [weather_forecast, get_the_time]

tool_node = ToolNode(tools)
