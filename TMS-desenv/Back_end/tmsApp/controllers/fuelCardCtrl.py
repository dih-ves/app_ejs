from flask import Blueprint, request, jsonify
import tmsApp.service.fuelCardService as fuelS
import tmsApp.controllers.authCtrl as authCtrl_7

CrudFuelCard = fuelS.CrudFuelCard
jwt_requerido = authCtrl_7.jwt_requerido
fuelCard_bp = Blueprint('fuelCard_bp', __name__)


@fuelCard_bp.route("/cartao_combustivel", methods=['GET'])
@jwt_requerido
def lista_fuelCards(data_user):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fuelCard = CrudFuelCard()
        listFuel = fuelCard.get_fuelCards()
        if listFuel is None:
            return {"mensagem": "nenhum cartão combustível encontrado"}, 204
        return jsonify(listFuel), 200
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@fuelCard_bp.route("/cartao_combustivel/<int:id_card>", methods=['GET'])
@jwt_requerido
def buscar(data_user, id_card):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fuelCard = CrudFuelCard()
        find = fuelCard.get_fuelCard(id_card)
        return find
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@fuelCard_bp.route("/cartao_combustivel/<int:id_card>", methods=['POST'])
@jwt_requerido
def inserir(data_user, id_card):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fuelCard = CrudFuelCard()
        dadosReq = request.json
        save = fuelCard.post_fuelCard(id_card, **dadosReq)
        return save
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@fuelCard_bp.route("/cartao_combustivel/<int:id_card>", methods=['PUT'])
@jwt_requerido
def alterar(data_user, id_card):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fuelCard = CrudFuelCard()
        dadosReq = request.json
        update = fuelCard.put_fuelCard(id_card, **dadosReq)
        return update
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


@fuelCard_bp.route("/cartao_combustivel/delete/<int:id_card>", methods=['DELETE'])
@jwt_requerido
def deletar(data_user, id_card):
    permissao_valida = verifica_permissao(data_user)
    if permissao_valida:
        fuelCard = CrudFuelCard()
        delete = fuelCard.del_fuelCard(id_card)
        return delete
    return {"mensagem": "voce nao possui acesso a este modulo"}, 403


def verifica_permissao(data_user):
    if data_user.get("grupo") == "admin":
        return True
    return False
