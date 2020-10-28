from flask import Blueprint, request, jsonify
import tmsApp.service.controlColabService as controlColabS
import tmsApp.controllers.authCtrl as authCtrl_11

CrudControlColab = controlColabS.CrudControlColab
jwt_requerido = authCtrl_11.jwt_requerido
controlColab_bp = Blueprint('controlColab_bp', __name__)


@controlColab_bp.route("/controle_colaborador", methods=['GET'])
@jwt_requerido
def lista_controlColabs(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        controlColab = CrudControlColab()
        listacontrolColab = controlColab.get_controlColabs()
        if listacontrolColab is None:
            return {"mensagem": "nenhum controle de colaborador  encontrado"}, 204
        return jsonify(listacontrolColab), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@controlColab_bp.route("/controle_colaborador/<int:id_control>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_control):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        controlColab = CrudControlColab()
        find = controlColab.get_controlColab(id_control)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@controlColab_bp.route("/controle_colaborador/colaborador/<int:colaborador_id>", methods=['GET'])
@jwt_requerido
def buscar_by_colaborador_id(data_user, colaborador_id):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        controlColab = CrudControlColab()
        find = controlColab.get_controlColab(colaborador_id)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@controlColab_bp.route("/controle_colaborador/<int:id_control>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_control):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        controlColab = CrudControlColab()
        dadosReq = request.json
        save = controlColab.post_controlColab(id_control, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@controlColab_bp.route("/controle_colaborador/<int:id_control>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_control):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        controlColab = CrudControlColab()
        dadosReq = request.json
        update = controlColab.put_controlColab(id_control, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@controlColab_bp.route("/controle_colaborador/delete/<int:id_control>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_control):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        controlColab = CrudControlColab()
        delete = controlColab.del_controlColab(id_control)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
