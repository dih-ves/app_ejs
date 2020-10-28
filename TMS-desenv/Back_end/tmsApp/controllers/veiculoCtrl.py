from flask import Blueprint, request, jsonify
import tmsApp.service.veiculoService as veiculoS
import tmsApp.controllers.authCtrl as authCtrl_2

CrudVeiculo = veiculoS.CrudVeiculo
jwt_requerido = authCtrl_2.jwt_requerido
veiculo_bp = Blueprint('veiculo_bp', __name__)


@veiculo_bp.route("/veiculo", methods=['GET'])
@jwt_requerido
def lista_veiculos(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        veiculo = CrudVeiculo()
        listaVeiculo = veiculo.get_veiculos()
        if listaVeiculo is None:
            return {"mensagem": "nenhum veiculo encontrado"}, 204
        return jsonify(listaVeiculo), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@veiculo_bp.route("/veiculo/<int:id_veiculo>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_veiculo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        veiculo = CrudVeiculo()
        find = veiculo.get_veiculo(id_veiculo)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@veiculo_bp.route("/veiculo/<int:id_veiculo>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_veiculo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        veiculo = CrudVeiculo()
        dadosReq = request.json
        save = veiculo.post_veiculo(id_veiculo, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@veiculo_bp.route("/veiculo/<int:id_veiculo>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_veiculo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        veiculo = CrudVeiculo()
        dadosReq = request.json
        update = veiculo.put_veiculo(id_veiculo, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@veiculo_bp.route("/veiculo/delete/<int:id_veiculo>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_veiculo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        veiculo = CrudVeiculo()
        delete = veiculo.del_veiculo(id_veiculo)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
