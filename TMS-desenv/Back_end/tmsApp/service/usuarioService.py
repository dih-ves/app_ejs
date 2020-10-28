import tmsApp.domain.repository.usuariodao as userdao
import tmsApp.domain.entities.usuario as user


class CrudUsuario:
    def __init__(self):
        self._errorMsg = None
        self._UsuarioDAO = userdao.UsuarioDAO
        self._Usuario = user.Usuario

    def cria_usuario(self, id_usuario, **Kwargs):
        try:
            usuario = self._Usuario(id_usuario, **Kwargs)
            return usuario
        except TypeError as e:
            self._errorMsg = str(e)
            return {"mensagem_de_erro": self._errorMsg}

    def get_usuarios(self):
        pesquisar = self._UsuarioDAO()
        lista = pesquisar.find_usuarios()
        return lista

    def get_usuario(self, id_usuario):
        pesquisar = self._UsuarioDAO()
        usuario = pesquisar.find_usuario(id_usuario)
        if usuario:
            return usuario, 200
        else:
            return {"mensagem": "usuario não encontrado"}, 404

    def post_usuario(self, id_usuario, **Kwargs):
        inserir = self._UsuarioDAO()
        usuario = self.cria_usuario(id_usuario, **Kwargs)
        if isinstance(usuario, self._Usuario):
            usuarioExiste = inserir.find_usuario(id_usuario)
            if usuarioExiste:
                return {"mensagem": "usuario já cadastrado"}, 400
            else:
                resultado = inserir.save_usuario(usuario)
                if resultado:
                    return {"mensagem": "usuario cadastrado com sucesso"}, 200
                else:
                    return {"mensagem_de_erro": inserir.get_error()}, 400
        return usuario, 400

    def put_usuario(self, id_usuario, **Kwargs):
        update = self._UsuarioDAO()
        usuario = self.cria_usuario(id_usuario, **Kwargs)
        if isinstance(usuario, self._Usuario):
            usuarioExiste = update.find_usuario(id_usuario)
            if usuarioExiste:
                resultado = update.update_usuario(usuario)
                if resultado:
                    return {"mensagem": "usuario atualizado"}, 201
                else:
                    return {"mensagem_de_erro": update.get_error()}, 400
            else:
                resultado = self.post_usuario(id_usuario, **Kwargs)
                return resultado
        return usuario, 400

    def del_usuario(self, id_usuario):
        delete = self._UsuarioDAO()
        usuario = delete.find_usuario(id_usuario)
        if usuario:
            delete.delete_usuario(id_usuario)
            return {"mensagem": "usuario removido"}, 200
        return {"mensagem": "usuario não encontrado"}, 404
