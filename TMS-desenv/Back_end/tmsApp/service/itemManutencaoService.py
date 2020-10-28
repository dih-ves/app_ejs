from tmsApp.domain.repository.itemManutencaodao import ItemManutencaoDAO
from tmsApp.domain.entities.itemManutencao import ItemManutencao


class CrudItemManutencao:
    def __init__(self):
        self._errorMsg = None

    def cria_itemManutencao(self, id_manutencao, **Kwargs):
        try:
            itemManutencao = ItemManutencao(id_manutencao, **Kwargs)
            return itemManutencao
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_itemManutencaos(self):
        pesquisar = ItemManutencaoDAO()
        lista = pesquisar.list_itemManutencao()
        return lista

    def get_itemManutencao(self, id_itemManutencao):
        pesquisar = ItemManutencaoDAO()
        itemManutencao = pesquisar.find_itemManutencao(id_itemManutencao)
        if itemManutencao:
            return itemManutencao, 200
        else:
            return {"mensagem": "item não encontrado"}, 404

    def post_itemManutencao(self, id_manutencao, **Kwargs):
        inserir = ItemManutencaoDAO()
        itemManutencao = self.cria_itemManutencao(id_manutencao, **Kwargs)
        if isinstance(itemManutencao, ItemManutencao):
            itemManutencaoExiste = inserir.find_itemManutencao(itemManutencao._id)
            if itemManutencaoExiste:
                return {"mensagem": "item já cadastrado"}, 400
            else:
                resultado = inserir.save_itemManutencao(itemManutencao)
                if resultado:
                    return {"mensagem": "item cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return itemManutencao, 400

    def put_itemManutencao(self, id_manutencao, **Kwargs):
        update = ItemManutencaoDAO()
        itemManutencao = self.cria_itemManutencao(id_manutencao, **Kwargs)
        if isinstance(itemManutencao, ItemManutencao):
            itemManutencaoExiste = update.find_itemManutencao(itemManutencao._id)
            if itemManutencaoExiste:
                resultado = update.update_itemManutencao(itemManutencao)
                if resultado:
                    return {"mensagem": "item atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_itemManutencao(id_itemManutencao, **Kwargs)
                return resultado
        return itemManutencao, 400

    def del_itemManutencao(self, id_itemManutencao):
        delete = ItemManutencaoDAO()
        itemManutencao = delete.find_itemManutencao(id_itemManutencao)
        if itemManutencao:
            delete.delete_itemManutencao(id_itemManutencao)
            return {"mensagem": "item removido"}, 200
        return {"mensagem": "item não encontrado"}, 404
