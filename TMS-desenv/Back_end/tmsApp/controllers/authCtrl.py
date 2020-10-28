from flask import Blueprint, request, jsonify
from functools import wraps
import tmsApp.service.authService as authService


auth_bp = Blueprint("auth_bp", __name__)
AutenticaUser = authService.AutenticaUser


def jwt_requerido(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        auth = AutenticaUser()
        auth_header = request.headers.get("Authorization")
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            auth = AutenticaUser()
            responseObject = auth.user_logado(auth_token)
            if responseObject[0].get("status") == "fail":
                return jsonify({"mensagem": "invalid token"}), 403
            return func(responseObject[0].get("data"), *args, **kwargs)
        return jsonify({"mensagem": "missing token"}), 403
    return wrapped


@auth_bp.route("/auth/login", methods=['POST'])
def login():
    auth = AutenticaUser()
    dadosReq = request.json
    login = auth.user_login(**dadosReq)
    return login[0], login[1]


@auth_bp.route("/auth/status", methods=['GET'])
@jwt_requerido
def status():
    auth = AutenticaUser()
    auth_header = request.headers.get("Authorization")
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        responseObject = auth.user_logado(auth_token)
        return responseObject[0], responseObject[1]

    else:
        responseObject = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return responseObject, 401


@auth_bp.route("/auth/logout", methods=['POST'])
def logout():
    auth = AutenticaUser()
    auth_header = request.headers.get("Authorization")
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        responseObject = auth.user_logout(auth_token)
        return responseObject[0], responseObject[1]

    else:
        responseObject = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return responseObject, 401
