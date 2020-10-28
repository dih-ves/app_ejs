from flask import Blueprint, request, jsonify
import tmsApp.service.combustivelService as combustivelS
import tmsApp.controllers.authCtrl as authCtrl_12

CrudCombustivel = combustivelS.CrudCombustivel
jwt_requerido = authCtrl_12.jwt_requerido
combustivel_bp = Blueprint('combustivel_bp', __name__)


@combustivel_bp.route("/combustivel", methods=['GET'])
@jwt_requerido
def lista_combustivels(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        combustivel = CrudCombustivel()
        listacomb = combustivel.get_combustiveis()
        if listacomb is None:
            return {"mensagem": "nenhum combustivel encontrado"}, 204
        return jsonify(listacomb), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@combustivel_bp.route("/combustivel/<int:ano>/<int:mes>", methods=['GET'])
@jwt_requerido
def lista_intervalo_combustivel(data_user, ano, mes):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        combustivel = CrudCombustivel()
        find = combustivel.get_intervalo_combustivel(ano, mes)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@combustivel_bp.route("/combustivel/<int:id_combustivel>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_combustivel):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        combustivel = CrudCombustivel()
        find = combustivel.get_combustivel(id_combustivel)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@combustivel_bp.route("/combustivel/<int:id_combustivel>", methods=['POST'])
@jwt_requerido
def inserir(idata_user, d_combustivel):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        combustivel = CrudCombustivel()
        dadosReq = request.json
        save = combustivel.post_combustivel(id_combustivel, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@combustivel_bp.route("/combustivel/<int:id_combustivel>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_combustivel):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        combustivel = CrudCombustivel()
        dadosReq = request.json
        update = combustivel.put_combustivel(id_combustivel, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@combustivel_bp.route("/combustivel/delete/<int:id_combustivel>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_combustivel):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        combustivel = CrudCombustivel()
        delete = combustivel.del_combustivel(id_combustivel)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
