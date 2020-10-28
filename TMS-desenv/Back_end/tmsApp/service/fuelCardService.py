from tmsApp.domain.repository.fuelCarddao import FuelCardDAO
from tmsApp.domain.entities.fuelCard import FuelCard


class CrudFuelCard:
    def __init__(self):
        self._errorMsg = None

    def cria_fuelCard(self, id_cartao, **Kwargs):
        try:
            fuelCard = FuelCard(id_cartao, **Kwargs)
            return fuelCard
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_fuelCards(self):
        pesquisar = FuelCardDAO()
        lista = pesquisar.list_fuelCard()
        return lista

    def get_fuelCard(self, id_cartao):
        pesquisar = FuelCardDAO()
        fuelCard = pesquisar.find_fuelCard(id_cartao)
        if fuelCard:
            return fuelCard, 200
        else:
            return {"mensagem": "cartão combustível não encontrado"}, 404

    def post_fuelCard(self, id_cartao, **Kwargs):
        inserir = FuelCardDAO()
        fuelCard = self.cria_fuelCard(id_cartao, **Kwargs)
        if isinstance(fuelCard, FuelCard):
            fuelCardExiste = inserir.find_fuelCard(id_cartao)
            if fuelCardExiste:
                return {"mensagem": "cartão combustível já cadastrado"}, 400
            else:
                resultado = inserir.save_fuelCard(fuelCard)
                if resultado:
                    return {"mensagem": "cartão combustível cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return fuelCard, 400

    def put_fuelCard(self, id_cartao, **Kwargs):
        update = FuelCardDAO()
        fuelCard = self.cria_fuelCard(id_cartao, **Kwargs)
        if isinstance(fuelCard, FuelCard):
            fuelCardExiste = update.find_fuelCard(id_cartao)
            if fuelCardExiste:
                resultado = update.update_fuelCard(fuelCard)
                if resultado:
                    return {"mensagem": "cartão combustível atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_fuelCard(id_cartao, **Kwargs)
                return resultado
        return fuelCard, 400

    def del_fuelCard(self, id_cartao):
        delete = FuelCardDAO()
        fuelCard = delete.find_fuelCard(id_cartao)
        if fuelCard:
            delete.delete_fuelCard(id_cartao)
            return {"mensagem": "cartão combustível removido"}, 200
        return {"mensagem": "cartão combustível não encontrado"}, 404
