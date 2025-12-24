
from tool_implimentation import get_time, calc, lookup_faq

state = {
    "last_goals":[],
    "last_tool_result":None,
    "last_location":None,
}
def update_goals(goal):
    """to keep the last 3 goals"""
    state["last_goals"].append(goal)
    if len(state["last_goals"])> 3:
        state["last_goals"].pop(0)
        
        

def model_decide_tool(user_input):
    """
    Simulates how a model decides which tool to call.
    Returns tool_name and arguments.
    """
    text = user_input.lower()
    if "converter that to utc" in text and state["last_location"]:
        return "get_time", {"location": "UTC"}

    if "time" in user_input:
        if "cape town" in user_input:
            return "get_time", {"location": "Cape Town"}
        elif "nairobi" in user_input:
            return "get_time", {"location": "Nairobi"}
        elif "utc" in user_input:
            return "get_time", {"location": "UTC"}
        
    #calculation part
    if any(op in user_input for op in ["+", "-", "*", "/"]):
        return "calc", {"expression": user_input}
    
    #FAQ
    if "what is" in user_input or "define" in user_input:
        return "lookup_faq", {"query": user_input}

    return None, None


def run_agent():
    print("\nHello! I'm AI Agent what can I help you 😊.\nIf you want to quit type 'exit'.\n")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        tool_name, args = model_decide_tool(user_input)
        if tool_name is None:
            print("Agent: I'm not sure which tool to use for that.")
            continue

        if tool_name == "get_time":
            tool_result = get_time(**args)
            if "error" not in tool_result:
                state["last_goals"] = args["location"]

        elif tool_name == "calc":
            tool_result = calc(**args)

        elif tool_name == "lookup_faq":
            tool_result = lookup_faq(**args)
            
        #to store
        state["last_tool_result"] = tool_result
        update_goals(tool_name)

        """Send tool result back to "model" and produce final answer
        with error handling & recovery"""
        
        if "error" in tool_result:
            print(f"Agent: {tool_result['error']}")
            print("Agent: Please try again with a valid input.\n")

        else:
            print(f"Agent: used {tool_name}\n{tool_result}")
        print(f"[Memory] Last goals: {state['last_goals']}")
        print(f"[Memory] Last location: {state['last_location']}")



if __name__ == "__main__":
    run_agent()
