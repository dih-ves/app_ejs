from flask import Blueprint, request, jsonify
import tmsApp.service.departamentoService as departamentoS
import tmsApp.controllers.authCtrl as authCtrl_9

CrudDepartamento = departamentoS.CrudDepartamento
jwt_requerido = authCtrl_9.jwt_requerido
departamento_bp = Blueprint('departamento_bp', __name__)


@departamento_bp.route("/departamento", methods=['GET'])
@jwt_requerido
def lista_departamentos(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        departamento = CrudDepartamento()
        listaDepartamento = departamento.get_departamentos()
        if listaDepartamento is None:
            return {"mensagem": "nenhum departamento encontrado"}, 204
        return jsonify(listaDepartamento), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@departamento_bp.route("/departamento/<int:id_departamento>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_departamento):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        departamento = CrudDepartamento()
        find = departamento.get_departamento(id_departamento)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@departamento_bp.route("/departamento/<int:id_departamento>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_departamento):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        departamento = CrudDepartamento()
        dadosReq = request.json
        save = departamento.post_departamento(id_departamento, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@departamento_bp.route("/departamento/<int:id_departamento>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_departamento):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        departamento = CrudDepartamento()
        dadosReq = request.json
        update = departamento.put_departamento(id_departamento, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@departamento_bp.route("/departamento/delete/<int:id_departamento>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_departamento):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        departamento = CrudDepartamento()
        delete = departamento.del_departamento(id_departamento)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
