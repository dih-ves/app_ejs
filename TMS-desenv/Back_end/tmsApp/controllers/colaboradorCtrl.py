from flask import Blueprint, request, jsonify
import tmsApp.service.colaboradorService as colaboradorS
import tmsApp.controllers.authCtrl as authCtrl_13

CrudColaborador = colaboradorS.CrudColaborador
jwt_requerido = authCtrl_13.jwt_requerido
colaborador_bp = Blueprint('colaborador_bp', __name__)


@colaborador_bp.route("/colaborador", methods=['GET'])
@jwt_requerido
def lista_colaboradores(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        colaborador = CrudColaborador()
        listaColab = colaborador.get_colaboradores()
        if listaColab is None:
            return {"mensagem": "nenhum colaborador encontrado"}, 204
        return jsonify(listaColab), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@colaborador_bp.route("/colaborador/<int:id_colaborador>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_colaborador):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        colaborador = CrudColaborador()
        find = colaborador.get_colaborador(id_colaborador)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@colaborador_bp.route("/colaborador/<int:id_colaborador>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_colaborador):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        colaborador = CrudColaborador()
        dadosReq = request.json
        save = colaborador.post_colaborador(id_colaborador, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@colaborador_bp.route("/colaborador/<int:id_colaborador>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_colaborador):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        colaborador = CrudColaborador()
        dadosReq = request.json
        update = colaborador.put_colaborador(id_colaborador, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@colaborador_bp.route("/colaborador/delete/<int:id_colaborador>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_colaborador):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        colaborador = CrudColaborador()
        delete = colaborador.del_colaborador(id_colaborador)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
