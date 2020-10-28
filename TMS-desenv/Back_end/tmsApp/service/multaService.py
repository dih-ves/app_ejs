from tmsApp.domain.repository.multadao import MultaDAO
from tmsApp.domain.entities.multa import Multa


class CrudMulta:
    def __init__(self):
        self._errorMsg = None

    def cria_multa(self, id_multa, **Kwargs):
        try:
            multa = Multa(id_multa, **Kwargs)
            return multa
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_multas(self):
        pesquisar = MultaDAO()
        lista = pesquisar.list_multa()
        return lista

    def get_multa(self, id_multa):
        pesquisar = MultaDAO()
        multa = pesquisar.find_multa(id_multa)
        if multa:
            return multa, 200
        else:
            return {"mensagem": "multa não encontrada"}, 404

    def post_multa(self, id_multa, **Kwargs):
        inserir = MultaDAO()
        multa = self.cria_multa(id_multa, **Kwargs)
        if isinstance(multa, Multa):
            multaExiste = inserir.find_multa(id_multa)
            if multaExiste:
                return {"mensagem": "multa já cadastrada"}, 400
            else:
                resultado = inserir.save_multa(multa)
                if resultado:
                    return {"mensagem": "multa cadastrada com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return multa, 400

    def put_multa(self, id_multa, **Kwargs):
        update = MultaDAO()
        multa = self.cria_multa(id_multa, **Kwargs)
        if isinstance(multa, Multa):
            multaExiste = update.find_multa(id_multa)
            if multaExiste:
                resultado = update.update_multa(multa)
                if resultado:
                    return {"mensagem": "multa atualizada"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_multa(id_multa, **Kwargs)
                return resultado
        return multa, 400

    def del_multa(self, id_multa):
        delete = MultaDAO()
        multa = delete.find_multa(id_multa)
        if multa:
            delete.delete_multa(id_multa)
            return {"mensagem": "multa removida"}, 200
        return {"mensagem": "multa não encontrada"}, 404
