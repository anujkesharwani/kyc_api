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


def serialize_nepal_pan_response(pan_info):
    """
    Serialize Nepal PAN verification response into a standardized format.

    Args:
        pan_info (dict): Dictionary containing PAN verification details

    Returns:
        dict: Standardized response format
    """
    if not isinstance(pan_info, dict):
        raise ValueError("Invalid PAN information format")

    return {
        "status": "success",
        "data": {
            "pan_number": pan_info.get("pan_number", ""),
            "trade_name_nep": pan_info.get("trade_name_nep", ""),
            "office_name": pan_info.get("office_name", ""),
            "ward_number": pan_info.get("ward_number", ""),
            "mobile_number": pan_info.get("mobile_number", ""),
            "street_name": pan_info.get("street_name", ""),
            "verification_date": pan_info.get("verification_date", ""),
            "verification_status": pan_info.get("verification_status", "verified")
        }
    }