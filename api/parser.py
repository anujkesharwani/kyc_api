from flask import request

def parse_verification_request():
    data = request.get_json()
    vc1 = data.get("vc1")
    vc2 = data.get("vc2")
    vc3 = data.get("vc3")
    vc4 = data.get("vc4")

    if not all([vc1, vc2, vc3, vc4]):
        raise ValueError("All fields (vc1, vc2, vc3, vc4) are required.")

    return vc1, vc2, vc3, vc4


def parse_nepal_pan_request():
    data = request.get_json()
    pan_number = data.get("pan_number")

    if not pan_number:
        raise ValueError("PAN number is required.")

    if not isinstance(pan_number, str) or not pan_number.isdigit():
        raise ValueError("PAN number must be a numeric string.")

    if len(pan_number) != 9:
        raise ValueError("PAN number must be 9 digits long.")

    return pan_number