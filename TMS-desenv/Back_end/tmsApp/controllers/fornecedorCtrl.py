from flask import Blueprint, request, jsonify
import tmsApp.service.fornecedorService as fornecedorS
import tmsApp.controllers.authCtrl as authCtrl_8

CrudFornecedor = fornecedorS.CrudFornecedor
jwt_requerido = authCtrl_8.jwt_requerido
fornecedor_bp = Blueprint('fornecedor_bp', __name__)


@fornecedor_bp.route("/fornecedor", methods=['GET'])
@jwt_requerido
def lista_fornecedores(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fornecedor = CrudFornecedor()
        listaFornec = fornecedor.get_fornecedores()
        if listaFornec is None:
            return {"mensagem": "nenhum fornecedor encontrado"}, 204
        return jsonify(listaFornec), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403



@fornecedor_bp.route("/fornecedor/<int:id_fornecedor>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_fornecedor):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fornecedor = CrudFornecedor()
        find = fornecedor.get_fornecedor(id_fornecedor)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@fornecedor_bp.route("/fornecedor/<int:id_fornecedor>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_fornecedor):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fornecedor = CrudFornecedor()
        dadosReq = request.json
        save = fornecedor.post_fornecedor(id_fornecedor, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@fornecedor_bp.route("/fornecedor/<int:id_fornecedor>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_fornecedor):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fornecedor = CrudFornecedor()
        dadosReq = request.json
        update = fornecedor.put_fornecedor(id_fornecedor, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@fornecedor_bp.route("/fornecedor/delete/<int:id_fornecedor>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_fornecedor):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fornecedor = CrudFornecedor()
        delete = fornecedor.del_fornecedor(id_fornecedor)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
