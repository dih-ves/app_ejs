from tmsApp.domain.repository.manutencaodao import ManutencaoDAO
from tmsApp.domain.entities.manutencao import Manutencao
from tmsApp.domain.entities.itemManutencao import ItemManutencao


class CrudManutencao:
    def __init__(self):
        self._errorMsg = None

    def cria_manutencao(self, id_manutencao, **Kwargs):
        try:
            manutencao = Manutencao(id_manutencao, **Kwargs)
            return manutencao
        except TypeError as e:
            self._errorMsg = str(e)
            return False

    def cria_item(self, id_manutencao, itens):
        listaItem = []
        try:
            for dicio in itens:
                item = ItemManutencao(id_manutencao, **dicio)
                listaItem.append(item)
            return listaItem
        except TypeError as e:
            self._errorMsg = str(e)
            return False

    def get_manutencoes(self):
        pesquisar = ManutencaoDAO()
        lista = pesquisar.list_manutencao()
        return lista

    def get_intervalo_manutencao(self, ano, mes):
        pesquisar = ManutencaoDAO()
        manutencao = pesquisar.list_intervalo_manutencao(ano, mes)
        if manutencao:
            return manutencao, 200
        else:
            return {"mensagem": "manutencao de Veiculo não encontrada"}, 404

    def get_manutencao(self, id_manutencao):
        pesquisar = ManutencaoDAO()
        manutencao = pesquisar.find_manutencao(id_manutencao)
        if manutencao:
            return manutencao, 200
        else:
            return {"mensagem": "manutencao de Veiculo não encontrada"}, 404

    def post_manutencao(self, id_manutencao, **Kwargs):
        itens = Kwargs.pop("item_manutencao")
        inserir = ManutencaoDAO()
        manutencao = self.cria_manutencao(id_manutencao, **Kwargs)
        listaItem = self.cria_item(id_manutencao, itens)
        if isinstance(manutencao, Manutencao) and isinstance(listaItem, list):
            manutencaoExiste = inserir.find_manutencao(id_manutencao)
            if manutencaoExiste:
                return {"mensagem": "manutencao de Veiculo já registrada"}, 400
            else:
                resultado = inserir.save_manutencao(manutencao, listaItem)
                if resultado:
                    return {"mensagem": "manutencao de Veiculo registrada com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return {"mensagem_de_erro": self.get_error()}, 400

    def put_manutencao(self, id_manutencao, **Kwargs):
        itens = Kwargs.pop("item_manutencao")
        update = ManutencaoDAO()
        manutencao = self.cria_manutencao(id_manutencao, **Kwargs)
        listaItem = self.cria_item(id_manutencao, itens)
        if isinstance(manutencao, Manutencao) and isinstance(listaItem, list):
            manutencaoExiste = update.find_manutencao(id_manutencao)
            if manutencaoExiste:
                novosItens, atuaisItens = self.filtra_itens(manutencaoExiste, listaItem)
                resultado = update.update_manutencao(manutencao, novosItens, atuaisItens)
                if resultado:
                    return {"mensagem": "manutencao de Veiculo atualizada"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                Kwargs["item_manutencao"] = dicioItem
                resultado = self.post_manutencao(id_manutencao, **Kwargs)
                return resultado
        return manutencao, 400

    def del_manutencao(self, id_manutencao):
        delete = ManutencaoDAO()
        manutencao = delete.find_manutencao(id_manutencao)
        if manutencao:
            delete.delete_manutencao(id_manutencao)
            return {"mensagem": "manutencao removida"}, 200
        return {"mensagem": "manutencao não encontrada"}, 404

    def get_error(self):
        return self._errorMsg

    def filtra_itens(self, manutencao, listaItem):
        newItem = []
        currentItem = []
        for novoItem in listaItem:
            exiteItem = [True for item in manutencao["item_manutencao"] if item["id"] == novoItem._id]
            if exiteItem:
                currentItem.append(novoItem)
            else:
                newItem.append(novoItem)
        return newItem, currentItem
