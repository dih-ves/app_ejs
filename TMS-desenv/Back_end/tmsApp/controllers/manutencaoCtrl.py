from flask import Blueprint, request, jsonify
import tmsApp.service.manutencaoService as manutencaoS
import tmsApp.controllers.authCtrl as authCtrl_5

CrudManutencao = manutencaoS.CrudManutencao
jwt_requerido = authCtrl_5.jwt_requerido
manutencao_bp = Blueprint('manutencao_bp', __name__)


@manutencao_bp.route("/manutencao_veiculo", methods=['GET'])
@jwt_requerido
def lista_manutencao(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        manutencao = CrudManutencao()
        listaManut = manutencao.get_manutencoes()
        if listaManut is None:
            return {"mensagem": "nenhuma manutencao de Veiculo encontrada"}, 204
        return jsonify(listaManut), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@manutencao_bp.route("/manutencao_veiculo/<int:ano>/<int:mes>", methods=['GET'])
@jwt_requerido
def lista_intervalo_manutencao(data_user, ano, mes):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        manutencao = CrudManutencao()
        find = manutencao.get_intervalo_manutencao(ano, mes)
        return jsonify(find[0]), find[1]
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@manutencao_bp.route("/manutencao_veiculo/<int:id_manutencao>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_manutencao):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        manutencao = CrudManutencao()
        find = manutencao.get_manutencao(id_manutencao)
        return jsonify(find[0]), find[1]
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@manutencao_bp.route("/manutencao_veiculo/<int:id_manutencao>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_manutencao):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        manutencao = CrudManutencao()
        dadosReq = request.json
        save = manutencao.post_manutencao(id_manutencao, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@manutencao_bp.route("/manutencao_veiculo/<int:id_manutencao>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_manutencao):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        manutencao = CrudManutencao()
        dadosReq = request.json
        update = manutencao.put_manutencao(id_manutencao, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@manutencao_bp.route("/manutencao_veiculo/delete/<int:id_manutencao>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_manutencao):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        manutencao = CrudManutencao()
        delete = manutencao.del_manutencao(id_manutencao)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
