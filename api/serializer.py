import json

def serialize_response(data):
    if isinstance(data, str):
        try:
            # If data is already a JSON string, parse it first
            data = json.loads(data)
        except json.JSONDecodeError:
            pass
    
    return {
        "status": "success",
        "data": data
    }
