from langchain.agents import Tool, AgentExecutor, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from tools.calculator import calculator_tool
from langchain_community.callbacks.manager import get_openai_callback



llm = ChatOpenAI(temperature=0)

tools = [calculator_tool]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent():
    user_query = "What is 20% of the average of 3, 7, and 11?"
    print(f"User Query: {user_query}")
    with get_openai_callback() as cb:
        result = agent.run(user_query)
        print(f"\nFinal Answer: {result}")
        print(f"\n📊 Token Usage Summary:\n{cb}")

if __name__ == "__main__":
    run_agent()