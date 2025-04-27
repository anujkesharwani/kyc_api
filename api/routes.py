from flask import Blueprint, jsonify
from api.parser import parse_verification_request, parse_nepal_pan_request
from api.serializer import serialize_response, serialize_nepal_pan_response
from verifier.haryana_labour import HaryanaLabour
from verifier.nepal_pan import ChildClass as NepalPanVerifier

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

@router.route('/nepal-pan', methods=['POST'])
def verify_nepal_pan():
    try:
        pan_number = parse_nepal_pan_request()
        verifier = NepalPanVerifier()
        verifier.pan = pan_number
        result = verifier.pre_query()
        return jsonify(serialize_nepal_pan_response(result))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400