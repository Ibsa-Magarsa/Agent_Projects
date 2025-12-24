from datetime import *

# -------------------------------
# Tool 1: get_time
# -------------------------------
def get_time(location):
    """
    Returns the current time for a given location.
    Supports hard-coded locations.
    """
    locations = {
        "nairobi": timezone(timedelta(hours=3)),     # EAT (UTC+3)
        "cape town": timezone(timedelta(hours=2)),   # SAST (UTC+2)
        "utc": timezone.utc,
        "new york": timezone(timedelta(hours=-5))    # EST (UTC-5, simplified)
    }

    loc_key = location.lower()

    if loc_key not in locations:
        return {"error": f"Location '{location}' is not supported."}

    current_time = datetime.now(locations[loc_key])
    return {
        "location": location,
        "time": current_time.strftime("%Y-%m-%d\t %H:%M:%S")
    }


# Tool 2: calc

def calc(expression):
    """
    Safely evaluates a mathematical expression.
    """
    try:
        # Only allow numbers and basic operators
        allowed_chars = "0123456789+-*/(). "
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Invalid characters in expression.")

        result = eval(expression)
        return {"expression": expression, "result": result}

    except Exception as e:
        return {"error": f"Invalid expression: {str(e)}"}


# -------------------------------
# Tool 3: lookup_faq
# -------------------------------
def lookup_faq(query):
    """
    Looks up an answer from a mocked FAQ knowledge base.
    """
    faq_kb = {
        "what is python": {
            "answer": "Python is a high-level programming language used for web, data science, and AI.",
            "source_title": "Intro to Python"
        },
        "what is an AI Agent": {
            "answer": "An AI agent is a system that perceives its environment and acts to achieve goals.",
            "source_title": "AI Fundamentals"
        }
    }

    key = query.lower()

    if key in faq_kb:
        return faq_kb[key]

    return {
        "answer": "Sorry, no matching FAQ entry was found.",
        "source_title": "FAQ System"
    }


# -------------------------------
# Direct Tool Calls (for testing)
# -------------------------------
if __name__ == "__main__":
    print("Testing get_time:")
    print(get_time("Cape Town"))
    print(get_time("Nairobi"))
    print(get_time("UTC"))
    print(get_time("Tokyo"))  # unsupported

    print("\nTesting calc:")
    print(calc("24500 * 0.18"))
    print(calc("10 + 5 / 2"))
    print(calc("10 + abc"))  # invalid

    print("\nTesting lookup_faq:")
    print(lookup_faq("What is Python"))
    print(lookup_faq("What is Java"))
