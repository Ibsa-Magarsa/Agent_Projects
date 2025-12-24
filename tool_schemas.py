""" Define tool schemas.
Create schemas for 3 tools: """

# get_time
get_time_schema = {
    "name": "get_time",
    "description": "Get the current time for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "Name of the city or timezone (e.g.,Addis Ababa, Nairobi)"
            }
        },
        "required": ["location"]
    }
}

# Tool 2: calc_schema
calc_schema = {
    "name": "calc",
    "description": "Evaluate a mathematical expression.",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Mathematical expression to evaluate (e.g., '24500 * 0.18')"
            }
        },
        "required": ["expression"]
    }
}

# Tool 3: lookup_faq
lookup_faq_schema = {
    "name": "lookup_faq",
    "description": "Look up an answer from a frequently asked questions knowledge base.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Question or keyword to search in the FAQ knowledge base"
            }
        },
        "required": ["query"]
    }
}

# Collect all schemas in a list
tool_schemas = [
    get_time_schema,
    calc_schema,
    lookup_faq_schema
]

# For quick verification
if __name__ == "__main__":
    from pprint import pprint
    pprint(tool_schemas)
