from langchain.tools import tool

@tool
def calculator_tool(expression: str) -> str:
    """Evaluates a basic math expression. Useful for percentages, averages, etc."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"