from tmsApp.domain.repository.cargodao import CargoDAO
from tmsApp.domain.entities.cargo import Cargo


class CrudCargo:
    def __init__(self):
        self._errorMsg = None

    def cria_cargo(self, id_cargo, **Kwargs):
        try:
            cargo = Cargo(id_cargo, **Kwargs)
            return cargo
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_cargos(self):
        pesquisar = CargoDAO()
        lista = pesquisar.list_cargo()
        return lista

    def get_cargo(self, id_cargo):
        pesquisar = CargoDAO()
        cargo = pesquisar.find_cargo(id_cargo)
        if cargo:
            return cargo, 200
        else:
            return {"mensagem": "cargo não encontrado"}, 404

    def post_cargo(self, id_cargo, **Kwargs):
        inserir = CargoDAO()
        cargo = self.cria_cargo(id_cargo, **Kwargs)
        if isinstance(cargo, Cargo):
            cargoExiste = inserir.find_cargo(id_cargo)
            if cargoExiste:
                return {"mensagem": "cargo já cadastrado"}, 400
            else:
                resultado = inserir.save_cargo(cargo)
                if resultado:
                    return {"mensagem": "cargo cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return cargo, 400

    def put_cargo(self, id_cargo, **Kwargs):
        update = CargoDAO()
        cargo = self.cria_cargo(id_cargo, **Kwargs)
        if isinstance(cargo, Cargo):
            cargoExiste = update.find_cargo(id_cargo)
            if cargoExiste:
                resultado = update.update_cargo(cargo)
                if resultado:
                    return {"mensagem": "cargo atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_cargo(id_cargo, **Kwargs)
                return resultado
        return cargo, 400

    def del_cargo(self, id_cargo):
        delete = CargoDAO()
        cargo = delete.find_cargo(id_cargo)
        if cargo:
            delete.delete_cargo(id_cargo)
            return {"mensagem": "cargo removido"}, 200
        return {"mensagem": "cargo não encontrado"}, 404
