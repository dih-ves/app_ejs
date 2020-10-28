from tmsApp.domain.repository.veiculodao import VeiculoDAO
from tmsApp.domain.entities.veiculo import Veiculo


class CrudVeiculo:
    def __init__(self):
        self._errorMsg = None

    def cria_veiculo(self, id_veiculo, **Kwargs):
        try:
            veiculo = Veiculo(id_veiculo, **Kwargs)
            return veiculo
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_veiculos(self):
        pesquisar = VeiculoDAO()
        lista = pesquisar.list_veiculo()
        return lista

    def get_veiculo(self, id_veiculo):
        pesquisar = VeiculoDAO()
        veiculo = pesquisar.find_veiculo(id_veiculo)
        if veiculo:
            return veiculo, 200
        else:
            return {"mensagem": "veiculo não encontrado"}, 204

    def post_veiculo(self, id_veiculo, **Kwargs):
        inserir = VeiculoDAO()
        veiculo = self.cria_veiculo(id_veiculo, **Kwargs)
        if isinstance(veiculo, Veiculo):
            veiculoExiste = inserir.find_veiculo(id_veiculo)
            if veiculoExiste:
                return {"mensagem": "veiculo já cadastrado"}, 400
            else:
                resultado = inserir.save_veiculo(veiculo)
                if resultado:
                    return {"mensagem": "veiculo cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return veiculo, 400

    def put_veiculo(self, id_veiculo, **Kwargs):
        update = VeiculoDAO()
        veiculo = self.cria_veiculo(id_veiculo, **Kwargs)
        if isinstance(veiculo, Veiculo):
            veiculoExiste = update.find_veiculo(id_veiculo)
            if veiculoExiste:
                resultado = update.update_veiculo(veiculo)
                if resultado:
                    return {"mensagem": "veiculo atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_veiculo(id_veiculo, **Kwargs)
                return resultado
        return veiculo, 400

    def del_veiculo(self, id_veiculo):
        delete = VeiculoDAO()
        veiculo = delete.find_veiculo(id_veiculo)
        if veiculo:
            delete.delete_veiculo(id_veiculo)
            return {"mensagem": "veiculo removido"}, 200
        return {"mensagem": "veiculo não encontrado"}, 204
