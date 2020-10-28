from tmsApp.domain.repository.clientedao import ClienteDAO
from tmsApp.domain.entities.cliente import Cliente


class CrudCliente:
    def __init__(self):
        self._errorMsg = None

    def cria_cliente(self, id_cliente, **Kwargs):
        try:
            cliente = Cliente(id_cliente, **Kwargs)
            return cliente
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_clientes(self):
        pesquisar = ClienteDAO()
        lista = pesquisar.list_cliente()
        return lista

    def get_cliente(self, id_cliente):
        pesquisar = ClienteDAO()
        cliente = pesquisar.find_cliente(id_cliente)
        if cliente:
            return cliente, 200
        else:
            return {"mensagem": "cliente não encontrado"}, 404

    def post_cliente(self, id_cliente, **Kwargs):
        inserir = ClienteDAO()
        cliente = self.cria_cliente(id_cliente, **Kwargs)
        if isinstance(cliente, Cliente):
            clienteExiste = inserir.find_cliente(id_cliente)
            if clienteExiste:
                return {"mensagem": "cliente já cadastrado"}, 400
            else:
                resultado = inserir.save_cliente(cliente)
                if resultado:
                    return {"mensagem": "cliente cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return cliente, 400

    def put_cliente(self, id_cliente, **Kwargs):
        update = ClienteDAO()
        cliente = self.cria_cliente(id_cliente, **Kwargs)
        if isinstance(cliente, Cliente):
            clienteExiste = update.find_cliente(id_cliente)
            if clienteExiste:
                resultado = update.update_cliente(cliente)
                if resultado:
                    return {"mensagem": "cliente atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_cliente(id_cliente, **Kwargs)
                return resultado
        return cliente, 400

    def del_cliente(self, id_cliente):
        delete = ClienteDAO()
        cliente = delete.find_cliente(id_cliente)
        if cliente:
            delete.delete_cliente(id_cliente)
            return {"mensagem": "cliente removido"}, 200
        return {"mensagem": "cliente não encontrado"}, 404
