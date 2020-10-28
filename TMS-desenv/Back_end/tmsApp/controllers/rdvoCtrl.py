from flask import Blueprint, request, jsonify
import tmsApp.service.rdvoService as rdvoS
import tmsApp.controllers.authCtrl as authCtrl_3

CrudRdvo = rdvoS.CrudRdvo
jwt_requerido = authCtrl_3.jwt_requerido
rdvo_bp = Blueprint('rdvo_bp', __name__)


@rdvo_bp.route("/rdvo", methods=['GET'])
@jwt_requerido
def lista_rdvos(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        rdvo = CrudRdvo()
        listaRdvo = rdvo.get_rdvos()
        if listaRdvo is None:
            return {"mensagem": "nenhum rdvo encontrado"}, 204
        return jsonify(listaRdvo), 200


@rdvo_bp.route("/rdvo/<int:ano>/<int:mes>", methods=['GET'])
@jwt_requerido
def lista_intervalo_rdvos(data_user, ano, mes):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        rdvo = CrudRdvo()
        listaRdvo = rdvo.get_intervalo_rdvos(ano, mes)
        return listaRdvo


@rdvo_bp.route("/rdvo/<int:id_rdvo>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_rdvo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        rdvo = CrudRdvo()
        find = rdvo.get_rdvo(id_rdvo)
        return find


@rdvo_bp.route("/rdvo/<int:id_rdvo>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_rdvo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        rdvo = CrudRdvo()
        dadosReq = request.json
        save = rdvo.post_rdvo(id_rdvo, **dadosReq)
        return save


@rdvo_bp.route("/rdvo/<int:id_rdvo>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_rdvo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        rdvo = CrudRdvo()
        dadosReq = request.json
        update = rdvo.put_rdvo(id_rdvo, **dadosReq)
        return update


@rdvo_bp.route("/rdvo/delete/<int:id_rdvo>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_rdvo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        rdvo = CrudRdvo()
        delete = rdvo.del_rdvo(id_rdvo)
        return delete


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
