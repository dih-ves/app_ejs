from flask import Blueprint, request, jsonify
import tmsApp.service.multaService as multaS
import tmsApp.controllers.authCtrl as authCtrl_4

CrudMulta = multaS.CrudMulta
jwt_requerido = authCtrl_4.jwt_requerido
multa_bp = Blueprint('multa_bp', __name__)


@multa_bp.route("/multa", methods=['GET'])
@jwt_requerido
def lista_multas(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        multa = CrudMulta()
        listaMultas = multa.get_multas()
        if listaMultas is None:
            return {"mensagem": "nenhum multa encontrada"}, 204
        return jsonify(listaMultas), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@multa_bp.route("/multa/<int:id_multa>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_multa):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        multa = CrudMulta()
        find = multa.get_multa(id_multa)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@multa_bp.route("/multa/<int:id_multa>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_multa):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        multa = CrudMulta()
        dadosReq = request.json
        save = multa.post_multa(id_multa, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@multa_bp.route("/multa/<int:id_multa>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_multa):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        multa = CrudMulta()
        dadosReq = request.json
        update = multa.put_multa(id_multa, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@multa_bp.route("/multa/delete/<int:id_multa>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_multa):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        multa = CrudMulta()
        delete = multa.del_multa(id_multa)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
