from flask import Blueprint, request, jsonify
import tmsApp.service.cargoService as cargoS
import tmsApp.controllers.authCtrl as authCtrl_15

CrudCargo = cargoS.CrudCargo
jwt_requerido = authCtrl_15.jwt_requerido
cargo_bp = Blueprint('cargo_bp', __name__)


@cargo_bp.route("/cargo", methods=['GET'])
@jwt_requerido
def lista_cargos(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cargo = CrudCargo()
        listaCargo = cargo.get_cargos()
        if listaCargo is None:
            return {"mensagem": "nenhum cargo encontrado"}, 204
        return jsonify(listaCargo), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cargo_bp.route("/cargo/<int:id_cargo>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_cargo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cargo = CrudCargo()
        find = cargo.get_cargo(id_cargo)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cargo_bp.route("/cargo/<int:id_cargo>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_cargo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cargo = CrudCargo()
        dadosReq = request.json
        save = cargo.post_cargo(id_cargo, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cargo_bp.route("/cargo/<int:id_cargo>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_cargo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cargo = CrudCargo()
        dadosReq = request.json
        update = cargo.put_cargo(id_cargo, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@cargo_bp.route("/cargo/delete/<int:id_cargo>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_cargo):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        cargo = CrudCargo()
        delete = cargo.del_cargo(id_cargo)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
