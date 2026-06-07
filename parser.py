import json

def parse_llm_response(response):
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "error": "Failed to parse LLM output."
        }