from tmsApp.domain.repository.combustiveldao import CombustivelDAO
from tmsApp.domain.entities.combustivel import Combustivel


class CrudCombustivel:
    def __init__(self):
        self._errorMsg = None

    def cria_combustivel(self, id_combustivel, **Kwargs):
        try:
            combustivel = Combustivel(id_combustivel, **Kwargs)
            return combustivel
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_combustiveis(self):
        pesquisar = CombustivelDAO()
        lista = pesquisar.list_combustivel()
        return lista

    def get_intervalo_combustivel(self, ano, mes):
        pesquisar = CombustivelDAO()
        combustivel = pesquisar.list_intervalo_combustivel(ano, mes)
        if combustivel:
            return combustivel, 200
        else:
            return {"mensagem": "combustivel não encontrado"}, 404

    def get_combustivel(self, id_combustivel):
        pesquisar = CombustivelDAO()
        combustivel = pesquisar.find_combustivel(id_combustivel)
        if combustivel:
            return combustivel, 200
        else:
            return {"mensagem": "combustivel não encontrado"}, 404

    def post_combustivel(self, id_combustivel, **Kwargs):
        inserir = CombustivelDAO()
        combustivel = self.cria_combustivel(id_combustivel, **Kwargs)
        if isinstance(combustivel, Combustivel):
            combustivelExiste = inserir.find_combustivel(id_combustivel)
            if combustivelExiste:
                return {"mensagem": "registro combustivel já cadastrado"}, 400
            else:
                resultado = inserir.save_combustivel(combustivel)
                if resultado:
                    return {"mensagem": "registro de combustivel cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return combustivel, 400

    def put_combustivel(self, id_combustivel, **Kwargs):
        update = CombustivelDAO()
        combustivel = self.cria_combustivel(id_combustivel, **Kwargs)
        if isinstance(combustivel, Combustivel):
            combustivelExiste = update.find_combustivel(id_combustivel)
            if combustivelExiste:
                resultado = update.update_combustivel(combustivel)
                if resultado:
                    return {"mensagem": " registro de combustivel atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_combustivel(id_combustivel, **Kwargs)
                return resultado
        return combustivel, 400

    def del_combustivel(self, id_combustivel):
        delete = CombustivelDAO()
        combustivel = delete.find_combustivel(id_combustivel)
        if combustivel:
            delete.delete_combustivel(id_combustivel)
            return {"mensagem": " registro de combustivel removido"}, 200
        return {"mensagem": "combustivel não encontrado"}, 404
