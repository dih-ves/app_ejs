from tmsApp.domain.repository.controlColabdao import ControlColabDAO
from tmsApp.domain.entities.controlColab import ControlColab


class CrudControlColab:
    def __init__(self):
        self._errorMsg = None

    def cria_controlColab(self, id_control, **Kwargs):
        try:
            controlColab = ControlColab(id_control, **Kwargs)
            return controlColab
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_controlColabs(self):
        pesquisar = ControlColabDAO()
        lista = pesquisar.list_controlColab()
        return lista

    def get_controlColab(self, id_control):
        pesquisar = ControlColabDAO()
        controlColab = pesquisar.find_controlColab(id_control)
        if controlColab:
            return controlColab, 200
        else:
            return {"mensagem": "controle de colaborador não encontrado"}, 204

    def get_controlColab_by_Colab_id(self, colaborador_id):
        pesquisar = ControlColabDAO()
        controlColab = pesquisar.find_controlColab(colaborador_id)
        if controlColab:
            return controlColab, 200
        else:
            return {"mensagem": "controle de colaborador não encontrado"}, 204

    def post_controlColab(self, id_control, **Kwargs):
        inserir = ControlColabDAO()
        controlColab = self.cria_controlColab(id_control, **Kwargs)
        if isinstance(controlColab, ControlColab):
            controlColabExiste = inserir.find_controlColab(id_control)
            if controlColabExiste:
                return {"mensagem": "controle de colaborador já cadastrado"}, 400
            else:
                resultado = inserir.save_controlColab(controlColab)
                if resultado:
                    return {"mensagem": "controle de colaborador cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return controlColab, 400

    def put_controlColab(self, id_control, **Kwargs):
        update = ControlColabDAO()
        controlColab = self.cria_controlColab(id_control, **Kwargs)
        if isinstance(controlColab, ControlColab):
            controlColabExiste = update.find_controlColab(id_control)
            if controlColabExiste:
                resultado = update.update_controlColab(controlColab)
                if resultado:
                    return {"mensagem": "controle de colaborador atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_controlColab(id_control, **Kwargs)
                return resultado
        return controlColab, 400

    def del_controlColab(self, id_control):
        delete = ControlColabDAO()
        controlColab = delete.find_controlColab(id_control)
        if controlColab:
            delete.delete_controlColab(id_control)
            return {"mensagem": "controle de colaborador removido"}, 200
        return {"mensagem": "controle de colaborador não encontrado"}, 204
