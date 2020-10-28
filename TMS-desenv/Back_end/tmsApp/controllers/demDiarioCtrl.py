from flask import Blueprint, request, jsonify
import tmsApp.service.demDiarioService as demDiarioS
import tmsApp.controllers.authCtrl as authCtrl_10

CrudDemDiario = demDiarioS.CrudDemDiario
jwt_requerido = authCtrl_10.jwt_requerido
demDiario_bp = Blueprint('demDiario_bp', __name__)


@demDiario_bp.route("/demonstrativo_diario", methods=['GET'])
@jwt_requerido
def lista_demsDiario(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        demDiario = CrudDemDiario()
        listaDemDiario = demDiario.get_demsDiario()
        if listaDemDiario is None:
            return {"mensagem": "nenhum Demonstrativo encontrado"}, 204
        return jsonify(listaDemDiario), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@demDiario_bp.route("/demonstrativo_diario/<int:ano>/<int:mes>", methods=['GET'])
@jwt_requerido
def lista_intervalo_demsDiario(data_user, ano, mes):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        demDiario = CrudDemDiario()
        find = demDiario.get_intervalo_demsDiario(ano, mes)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@demDiario_bp.route("/demonstrativo_diario/<int:id_demDiario>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_demDiario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        demDiario = CrudDemDiario()
        find = demDiario.get_demDiario(id_demDiario)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@demDiario_bp.route("/demonstrativo_diario/<int:id_demDiario>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_demDiario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        demDiario = CrudDemDiario()
        dadosReq = request.json
        save = demDiario.post_demDiario(id_demDiario, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@demDiario_bp.route("/demonstrativo_diario/<int:id_demDiario>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_demDiario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        demDiario = CrudDemDiario()
        dadosReq = request.json
        update = demDiario.put_demDiario(id_demDiario, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@demDiario_bp.route("/demonstrativo_diario/delete/<int:id_demDiario>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_demDiario):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        demDiario = CrudDemDiario()
        delete = demDiario.del_demDiario(id_demDiario)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
