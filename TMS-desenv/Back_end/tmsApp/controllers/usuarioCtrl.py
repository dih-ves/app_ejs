from flask import Blueprint, request, jsonify
import tmsApp.service.usuarioService as userService
import tmsApp.controllers.authCtrl as authCtrl_1

CrudUsuario = userService.CrudUsuario
jwt_requerido = authCtrl_1.jwt_requerido
usuario_bp = Blueprint('usuario_bp', __name__)


@usuario_bp.route("/usuario", methods=['GET'])
@jwt_requerido
def lista_usuarios(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        usuario = CrudUsuario()
        listaUsuarios = usuario.get_usuarios()
        if listaUsuarios is None:
            return {"mensagem": "nenhum usuario encontrado"}, 204
        return jsonify(listaUsuarios), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@usuario_bp.route("/usuario/<int:id_usuario>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_usuario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        usuario = CrudUsuario()
        find = usuario.get_usuario(id_usuario)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@usuario_bp.route("/usuario/<int:id_usuario>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_usuario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        usuario = CrudUsuario()
        dadosReq = request.json
        save = usuario.post_usuario(id_usuario, **dadosReq)
        return jsonify(save[0]), save[1]
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@usuario_bp.route("/usuario/<int:id_usuario>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_usuario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        usuario = CrudUsuario()
        dadosReq = request.json
        update = usuario.put_usuario(id_usuario, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@usuario_bp.route("/usuario/delete/<int:id_usuario>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_usuario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        usuario = CrudUsuario()
        delete = usuario.del_usuario(id_usuario)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
