from tmsApp.domain.repository.grupodao import GrupoDAO
from tmsApp.domain.entities.grupo import Grupo


class CrudGrupo:
    def __init__(self):
        self._errorMsg = None

    def cria_grupo(self, id_grupo, **Kwargs):
        try:
            grupo = Grupo(id_grupo, **Kwargs)
            return grupo
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_grupos(self):
        pesquisar = GrupoDAO()
        lista = pesquisar.list_grupo()
        return lista

    def get_grupo(self, id_grupo):
        pesquisar = GrupoDAO()
        grupo = pesquisar.find_grupo(id_grupo)
        if grupo:
            return grupo, 200
        else:
            return {"mensagem": "grupo não encontrado"}, 404

    def post_grupo(self, id_grupo, **Kwargs):
        inserir = GrupoDAO()
        grupo = self.cria_grupo(id_grupo, **Kwargs)
        if isinstance(grupo, Grupo):
            grupoExiste = inserir.find_grupo(id_grupo)
            if grupoExiste:
                return {"mensagem": "grupo já cadastrado"}, 400
            else:
                resultado = inserir.save_grupo(grupo)
                if resultado:
                    return {"mensagem": "grupo cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return grupo, 400

    def put_grupo(self, id_grupo, **Kwargs):
        update = GrupoDAO()
        grupo = self.cria_grupo(id_grupo, **Kwargs)
        if isinstance(grupo, Grupo):
            grupoExiste = update.find_grupo(id_grupo)
            if grupoExiste:
                resultado = update.update_grupo(grupo)
                if resultado:
                    return {"mensagem": "grupo atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_grupo(id_grupo, **Kwargs)
                return resultado
        return grupo, 400

    def del_grupo(self, id_grupo):
        delete = GrupoDAO()
        grupo = delete.find_grupo(id_grupo)
        if grupo:
            delete.delete_grupo(id_grupo)
            return {"mensagem": "grupo removido"}, 200
        return {"mensagem": "grupo não encontrado"}, 404
