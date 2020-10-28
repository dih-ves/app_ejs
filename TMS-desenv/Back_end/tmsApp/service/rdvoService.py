from tmsApp.domain.repository.rdvodao import RdvoDAO
from tmsApp.domain.entities.rdvo import Rdvo


class CrudRdvo:
    def __init__(self):
        self._errorMsg = None

    def cria_rdvo(self, id_rdvo, **Kwargs):
        try:
            rdvo = Rdvo(id_rdvo, **Kwargs)
            return rdvo
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_rdvos(self):
        pesquisar = RdvoDAO()
        lista = pesquisar.list_rdvo()
        return lista

    def get_intervalo_rdvos(self, ano, mes):
        pesquisar = RdvoDAO()
        rdvo = pesquisar.list_intervalo_rdvo(ano, mes)
        if rdvo:
            return rdvo, 200
        else:
            return {"mensagem": "rdvo não encontrado"}, 404

    def get_rdvo(self, id_rdvo):
        pesquisar = RdvoDAO()
        rdvo = pesquisar.find_rdvo(id_rdvo)
        if rdvo:
            return rdvo, 200
        else:
            return {"mensagem": "rdvo não encontrado"}, 404

    def post_rdvo(self, id_rdvo, **Kwargs):
        inserir = RdvoDAO()
        rdvo = self.cria_rdvo(id_rdvo, **Kwargs)
        if isinstance(rdvo, Rdvo):
            rdvoExiste = inserir.find_rdvo(id_rdvo)
            if rdvoExiste:
                return {"mensagem": "rdvo já cadastrado"}, 400
            else:
                resultado = inserir.save_rdvo(rdvo)
                if resultado:
                    return {"mensagem": "rdvo cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return rdvo, 400

    def put_rdvo(self, id_rdvo, **Kwargs):
        update = RdvoDAO()
        rdvo = self.cria_rdvo(id_rdvo, **Kwargs)
        if isinstance(rdvo, Rdvo):
            rdvoExiste = update.find_rdvo(id_rdvo)
            if rdvoExiste:
                resultado = update.update_rdvo(rdvo)
                if resultado:
                    return {"mensagem": "rdvo atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_rdvo(id_rdvo, **Kwargs)
                return resultado
        return rdvo, 400

    def del_rdvo(self, id_rdvo):
        delete = RdvoDAO()
        rdvo = delete.find_rdvo(id_rdvo)
        if rdvo:
            delete.delete_rdvo(id_rdvo)
            return {"mensagem": "rdvo removido"}, 200
        return {"mensagem": "rdvo não encontrado"}, 404
