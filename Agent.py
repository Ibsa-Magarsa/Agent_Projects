
from tool_implimentation import get_time, calc, lookup_faq


def model_decide_tool(user_input):
    """
    Simulates how a model decides which tool to call.
    Returns tool_name and arguments.
    """
    user_input = user_input.lower()

    if "time" in user_input:
        if "cape town" in user_input:
            return "get_time", {"location": "Cape Town"}
        elif "nairobi" in user_input:
            return "get_time", {"location": "Nairobi"}
        elif "utc" in user_input:
            return "get_time", {"location": "UTC"}

    if any(op in user_input for op in ["+", "-", "*", "/"]):
        return "calc", {"expression": user_input}

    if "what is" in user_input or "define" in user_input:
        return "lookup_faq", {"query": user_input}

    return None, None


def run_agent():
    print("Tutor Agent is running. Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        tool_name, args = model_decide_tool(user_input)

        if tool_name == "get_time":
            tool_result = get_time(**args)

        elif tool_name == "calc":
            tool_result = calc(**args)

        elif tool_name == "lookup_faq":
            tool_result = lookup_faq(**args)

        else:
            print("Agent: I'm not sure which tool to use for that.")
            continue

        # Send tool result back to "model" and produce final answer
        if "error" in tool_result:
            print(f"Agent: {tool_result['error']}")
        else:
            print(f"Agent (using {tool_name}): {tool_result}")


if __name__ == "__main__":
    run_agent()
