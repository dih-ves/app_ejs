from tmsApp.domain.repository.colaboradordao import ColaboradorDAO
from tmsApp.domain.entities.colaborador import Colaborador


class CrudColaborador:
    def __init__(self):
        self._errorMsg = None

    def cria_colaborador(self, id_colaborador, **Kwargs):
        try:
            colaborador = Colaborador(id_colaborador, **Kwargs)
            return colaborador
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_colaboradores(self):
        pesquisar = ColaboradorDAO()
        lista = pesquisar.list_colaborador()
        return lista

    def get_colaborador(self, id_colaborador):
        pesquisar = ColaboradorDAO()
        colaborador = pesquisar.find_colaborador(id_colaborador)
        if colaborador:
            return colaborador, 200
        else:
            return {"mensagem": "colaborador não encontrado"}, 404

    def post_colaborador(self, id_colaborador, **Kwargs):
        inserir = ColaboradorDAO()
        colaborador = self.cria_colaborador(id_colaborador, **Kwargs)

        if isinstance(colaborador, Colaborador):
            colabExiste = inserir.find_colaborador(id_colaborador)
            if colabExiste:
                return {"mensagem": "colaborador já cadastrado"}, 400
            else:
                resultado = inserir.save_colaborador(colaborador)
                if resultado:
                    return {"mensagem": "colaborador cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return colaborador, 400

    def put_colaborador(self, id_colaborador, **Kwargs):
        update = ColaboradorDAO()
        colaborador = self.cria_colaborador(id_colaborador, **Kwargs)
        if isinstance(colaborador, Colaborador):
            colabExiste = update.find_colaborador(id_colaborador)
            if colabExiste:
                resultado = update.update_colaborador(colaborador)
                if resultado:
                    return {"mensagem": "colaborador atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_colaborador(id_colaborador, **Kwargs)
                return resultado
        return colaborador, 400

    def del_colaborador(self, id_colaborador):
        delete = ColaboradorDAO()
        colaborador = delete.find_colaborador(id_colaborador)
        if colaborador:
            delete.delete_colaborador(id_colaborador)
            return {"mensagem": "colaborador removido"}, 200
        return {"mensagem": "colaborador não encontrado"}, 404
