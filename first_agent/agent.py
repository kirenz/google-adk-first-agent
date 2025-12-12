from google.adk.agents.llm_agent import Agent
from first_agent.tools import get_current_time


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    # Brief description of what the agent can do (helpful in multi-agent systems)
    description="A helpful assistant that can tell the current time.",
    # The 'personality' and behavioral instructions for the agent.
    # These instructions influence HOW the agent responds.
    instruction="""
    You are a helpful assistant.
    When the user asks for the time, use the 'get_current_time' tool.
    You yourself do NOT know what time it is - you MUST use the tool!
    Respond in the same language as the user's question.
    Be friendly and precise in your response.
    """,
    tools=[get_current_time],
)
