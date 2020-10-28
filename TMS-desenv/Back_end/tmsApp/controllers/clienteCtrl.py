from flask import Blueprint, request, jsonify
import tmsApp.service.clienteService as clienteS
import tmsApp.controllers.authCtrl as authCtrl_14

CrudCliente = clienteS.CrudCliente
jwt_requerido = authCtrl_14.jwt_requerido
cliente_bp = Blueprint('cliente_bp', __name__)


@cliente_bp.route("/cliente", methods=['GET'])
@jwt_requerido
def lista_clientes(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cliente = CrudCliente()
        listaCliente = cliente.get_clientes()
        if listaCliente is None:
            return {"mensagem": "nenhum cliente encontrado"}, 204
        return jsonify(listaCliente), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cliente_bp.route("/cliente/<int:id_cliente>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_cliente):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cliente = CrudCliente()
        find = cliente.get_cliente(id_cliente)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cliente_bp.route("/cliente/<int:id_cliente>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_cliente):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cliente = CrudCliente()
        dadosReq = request.json
        save = cliente.post_cliente(id_cliente, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cliente_bp.route("/cliente/<int:id_cliente>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_cliente):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cliente = CrudCliente()
        dadosReq = request.json
        update = cliente.put_cliente(id_cliente, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cliente_bp.route("/cliente/delete/<int:id_cliente>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_cliente):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cliente = CrudCliente()
        delete = cliente.del_cliente(id_cliente)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
