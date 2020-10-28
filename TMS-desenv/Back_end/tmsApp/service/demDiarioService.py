from tmsApp.domain.repository.demDiariodao import DemDiarioDAO
from tmsApp.domain.entities.demDiario import DemDiario


class CrudDemDiario:
    def __init__(self):
        self._errorMsg = None

    def cria_demDiario(self, id_demDiario, **Kwargs):
        try:
            demDiario = DemDiario(id_demDiario, **Kwargs)
            return demDiario
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_demsDiario(self):
        pesquisar = DemDiarioDAO()
        lista = pesquisar.list_demonstrativo_diario()
        return lista

    def get_intervalo_demsDiario(self, ano, mes):
        pesquisar = DemDiarioDAO()
        demDiario = pesquisar.list_intervalo_demonstrativo_diario(ano, mes)
        if demDiario:
            return demDiario, 200
        else:
            return {"mensagem": "demonstrativo Diario não encontrado"}, 404

    def get_demDiario(self, id_demDiario):
        pesquisar = DemDiarioDAO()
        demDiario = pesquisar.find_demonstrativo_diario(id_demDiario)
        if demDiario:
            return demDiario, 200
        else:
            return {"mensagem": "demonstrativo Diario não encontrado"}, 404

    def post_demDiario(self, id_demDiario, **Kwargs):
        inserir = DemDiarioDAO()
        demDiario = self.cria_demDiario(id_demDiario, **Kwargs)
        if isinstance(demDiario, DemDiario):
            demExiste = inserir.find_demonstrativo_diario(id_demDiario)
            if demExiste:
                return {"mensagem": "demonstrativo Diario já registrado"}, 400
            else:
                resultado = inserir.save_demonstrativo_diario(demDiario)
                if resultado:
                    return {"mensagem": "demonstrativo Diario registrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return demDiario, 400

    def put_demDiario(self, id_demDiario, **Kwargs):
        update = DemDiarioDAO()
        demDiario = self.cria_demDiario(id_demDiario, **Kwargs)
        if isinstance(demDiario, DemDiario):
            demExiste = update.find_demonstrativo_diario(id_demDiario)
            if demExiste:
                resultado = update.update_demonstrativo_diario(demDiario)
                if resultado:
                    return {"mensagem": "Demonstrativo atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_demDiario(id_demDiario, **Kwargs)
                return resultado
        return demDiario, 400

    def del_demDiario(self, id_veiculo):
        delete = DemDiarioDAO()
        demDiario = delete.find_demonstrativo_diario(id_veiculo)
        if demDiario:
            delete.delete_demonstrativo_diario(id_veiculo)
            return {"mensagem": "Demonstrativo removido"}, 200
        return {"mensagem": "Demonstrativo Diario não encontrado"}, 404
