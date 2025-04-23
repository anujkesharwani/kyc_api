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
