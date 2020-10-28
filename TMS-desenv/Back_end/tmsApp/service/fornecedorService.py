from tmsApp.domain.repository.fornecedordao import FornecedorDAO
from tmsApp.domain.entities.fornecedor import Fornecedor


class CrudFornecedor:
    def __init__(self):
        self._errorMsg = None

    def cria_fornecedor(self, id_fornecedor, **Kwargs):
        try:
            fornecedor = Fornecedor(id_fornecedor, **Kwargs)
            return fornecedor
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_fornecedores(self):
        pesquisar = FornecedorDAO()
        lista = pesquisar.list_fornecedor()
        return lista

    def get_fornecedor(self, id_fornecedor):
        pesquisar = FornecedorDAO()
        fornecedor = pesquisar.find_fornecedor(id_fornecedor)
        if fornecedor:
            return fornecedor, 200
        else:
            return {"mensagem": "fornecedor não encontrado"}, 404

    def post_fornecedor(self, id_fornecedor, **Kwargs):
        inserir = FornecedorDAO()
        fornecedor = self.cria_fornecedor(id_fornecedor, **Kwargs)
        if isinstance(fornecedor, Fornecedor):
            fornecedorExiste = inserir.find_fornecedor(id_fornecedor)
            if fornecedorExiste:
                return {"mensagem": "fornecedor já cadastrado"}, 400
            else:
                resultado = inserir.save_fornecedor(fornecedor)
                if resultado:
                    return {"mensagem": "fornecedor cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return fornecedor, 400

    def put_fornecedor(self, id_fornecedor, **Kwargs):
        update = FornecedorDAO()
        fornecedor = self.cria_fornecedor(id_fornecedor, **Kwargs)
        if isinstance(fornecedor, Fornecedor):
            fornecedorExiste = update.find_fornecedor(id_fornecedor)
            if fornecedorExiste:
                resultado = update.update_fornecedor(fornecedor)
                if resultado:
                    return {"mensagem": "fornecedor atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_fornecedor(id_fornecedor, **Kwargs)
                return resultado
        return fornecedor, 400

    def del_fornecedor(self, id_fornecedor):
        delete = FornecedorDAO()
        fornecedor = delete.find_fornecedor(id_fornecedor)
        if fornecedor:
            delete.delete_fornecedor(id_fornecedor)
            return {"mensagem": "fornecedor removido"}, 200
        return {"mensagem": "fornecedor não encontrado"}, 404
