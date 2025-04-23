from flask import Blueprint, jsonify
from api.parser import parse_verification_request
from api.serializer import serialize_response
from verifier.haryana_labour import HaryanaLabour

router = Blueprint('router', __name__)

@router.route('/verify', methods=['POST'])
def verify_shop():
    try:
        vc1, vc2, vc3, vc4 = parse_verification_request()
        verifier = HaryanaLabour(vc1, vc2, vc3, vc4)
        result = verifier.pre_request()
        return jsonify(serialize_response(result))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
