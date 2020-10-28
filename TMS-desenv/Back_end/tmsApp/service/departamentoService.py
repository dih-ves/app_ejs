from tmsApp.domain.repository.departamentodao import DepartamentoDAO
from tmsApp.domain.entities.departamento import Departamento


class CrudDepartamento:
    def __init__(self):
        self._errorMsg = None

    def cria_departamento(self, id_departamento, **Kwargs):
        try:
            departamento = Departamento(id_departamento, **Kwargs)
            return departamento
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_departamentos(self):
        pesquisar = DepartamentoDAO()
        lista = pesquisar.list_departamento()
        return lista

    def get_departamento(self, id_departamento):
        pesquisar = DepartamentoDAO()
        departamento = pesquisar.find_departamento(id_departamento)
        if departamento:
            return departamento, 200
        else:
            return {"mensagem": "departamento não encontrado"}, 404

    def post_departamento(self, id_departamento, **Kwargs):
        inserir = DepartamentoDAO()
        departamento = self.cria_departamento(id_departamento, **Kwargs)
        if isinstance(departamento, Departamento):
            departamentoExiste = inserir.find_departamento(id_departamento)
            if departamentoExiste:
                return {"mensagem": "departamento já cadastrado"}, 400
            else:
                resultado = inserir.save_departamento(departamento)
                if resultado:
                    return {"mensagem": "departamento cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return departamento, 400

    def put_departamento(self, id_departamento, **Kwargs):
        update = DepartamentoDAO()
        departamento = self.cria_departamento(id_departamento, **Kwargs)
        if isinstance(departamento, Departamento):
            departamentoExiste = update.find_departamento(id_departamento)
            if departamentoExiste:
                resultado = update.update_departamento(departamento)
                if resultado:
                    return {"mensagem": "departamento atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_departamento(id_departamento, **Kwargs)
                return resultado
        return departamento, 400

    def del_departamento(self, id_departamento):
        delete = DepartamentoDAO()
        departamento = delete.find_departamento(id_departamento)
        if departamento:
            delete.delete_departamento(id_departamento)
            return {"mensagem": "departamento removido"}, 200
        return {"mensagem": "departamento não encontrado"}, 404
