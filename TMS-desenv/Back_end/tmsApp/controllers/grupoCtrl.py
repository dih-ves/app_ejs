from flask import Blueprint, request, jsonify
import tmsApp.service.grupoService as grupoS
import tmsApp.controllers.authCtrl as authCtrl_6

CrudGrupo = grupoS.CrudGrupo
jwt_requerido = authCtrl_6.jwt_requerido
grupo_bp = Blueprint('grupo_bp', __name__)


@grupo_bp.route("/grupo", methods=['GET'])
@jwt_requerido
def lista_grupos(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        grupo = CrudGrupo()
        listaGrupo = grupo.get_grupos()
        if listaGrupo is None:
            return {"mensagem": "nenhum grupo encontrado"}, 204
        return jsonify(listaGrupo), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@grupo_bp.route("/grupo/<int:id_grupo>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_grupo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        grupo = CrudGrupo()
        find = grupo.get_grupo(id_grupo)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@grupo_bp.route("/grupo/<int:id_grupo>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_grupo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        grupo = CrudGrupo()
        dadosReq = request.json
        save = grupo.post_grupo(id_grupo, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@grupo_bp.route("/grupo/<int:id_grupo>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_grupo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        grupo = CrudGrupo()
        dadosReq = request.json
        update = grupo.put_grupo(id_grupo, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@grupo_bp.route("/grupo/delete/<int:id_grupo>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_grupo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        grupo = CrudGrupo()
        delete = grupo.del_grupo(id_grupo)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
