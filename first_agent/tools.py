import datetime


def get_current_time() -> dict:
    """
    Returns the current time.

    This function is automatically called by the agent when the user
    asks for the current time. The agent:
    1. Recognizes the user's intent (wanting to know the time)
    2. Calls this function
    3. Receives the current system time
    4. Formulates a natural response based on the result

    Returns:
        Dictionary with status and current time
    """
    # Get current system time and format as string
    # strftime() formats the time: %H = hour (24h), %M = minute
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Return as dictionary - the agent uses this data for its response
    return {"status": "success", "time": current_time}
