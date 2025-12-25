
from tool_implimentation import get_time, calc, lookup_faq
import os
import re
state = {
    "last_goals":[],
    "last_tool_result":None,
    "last_location":None,
}
def update_goals(goal):
    """to keep the last 3 goals by creating a memory"""
    if not isinstance(state["last_goals"], list):
        state["last_goals"] = []

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

    if "time" in text:
        if "cape town" in text:
            return "get_time", {"location": "Cape Town"}
        elif "nairobi" in text:
            return "get_time", {"location": "Nairobi"}
        elif "utc" in text:
            return "get_time", {"location": "UTC"}
        
        
    #calculation part
    elif any(op in text for op in ["+", "-", "*", "/"]):
        return "calc", {"expression": user_input}
    
    #FAQ
    elif "what is" in text or "define" in text:
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
        
        if "%" in user_input :#and "of" in user_input:
                # try:
                raw_numbers = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+',user_input)
                numbers = [float(num.replace(',', '')) for num in raw_numbers]

                a, b = numbers
                print(f"\n📘 Question: {a}% of {b}\n")
                
                # Step 1
                print("Step 1️⃣: Understand what percent means")
                print("Percent (%) means 'per 100'")

                # Step 2
                decimal = a / 100
                print(f"\nStep 2️⃣: Convert {a}% to decimal")
                print(f"{a}% = {a} ÷ 100 = {decimal}")

                # Step 3
                result = decimal * b
                print(f"\nStep 3️⃣: Multiply the decimal by {b}")
                print(f"{decimal} × {b} = {result}")

                # Final Answer
                print(f"\n✅ Final Answer:")
                print(f"{a}% of {b} = {result}")
                continue
    
        # except Exception:
                
                # return None, None
                
        elif tool_name is None:
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
            
        # To store
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
        continue


if __name__ == "__main__":
    run_agent()
    
