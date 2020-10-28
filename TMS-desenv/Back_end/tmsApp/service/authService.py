
import tmsApp.domain.repository.usuariodao as userdao
import tmsApp.domain.entities.usuario as user
import tmsApp.service.usuarioService as userService
import tmsApp.domain.entities.blacklistToken as blacklist
import tmsApp.domain.repository.blacklistTokendao as blacklistdao


CrudUsuario = userService.CrudUsuario
UsuarioDAO = userdao.UsuarioDAO
blacklistTokenDAO = blacklistdao.BlacklistTokenDAO


class AutenticaUser(CrudUsuario):
    def valida_formato_senha(self, senha):
        valida = False
        goodChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        try:
            for letra in senha:
                if letra not in goodChars:
                    return valida
            valida = True
            return valida
        except (TypeError, ValueError):
            return valida

    def user_login(self, **Kwargs):
        logar = self._UsuarioDAO()
        usuarioExiste = logar.find_usuario_to_auth(Kwargs.get("user_name"))
        validado = self.valida_formato_senha(Kwargs.get("senha"))
        if usuarioExiste:
            usuario = self.cria_usuario(usuarioExiste.pop("id"), **usuarioExiste)
            if validado:
                if usuarioExiste and Kwargs.get("senha") == usuario._senha:
                    auth_token = usuario.encode_auth_token(usuario._id)
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully registered.',
                        'auth_token': auth_token.decode()
                    }
                    return responseObject, 200
                return {"mensagem":"usuario ou senha invalidos"}, 400
            return {"mensagem": "usuario ou senha invalidos"}, 400
        return {"mensagem": "usuario ou senha invalidos"}, 400

    def user_logado(self, auth_token):
        resp = user.Usuario.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            usuarioExiste = UsuarioDAO()
            usuario = usuarioExiste.find_usuario(resp)
            responseObject = {
                'status': 'success',
                'data': {
                    'user_id': usuario["id"],
                    'email': usuario["email"],
                    'grupo': usuario["grupo"]
                }
            }
            return responseObject, 200
        responseObject = {
            'status': 'fail',
            'message': resp
        }
        return responseObject, 401

    def user_logout(self, auth_token):
        resp = user.Usuario.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            blacklistToken = blacklist.BlacklistToken(auth_token)
            save_in_blacklist = blacklistTokenDAO()
            responseObject = save_in_blacklist.save_token(blacklistToken)
            if responseObject:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged out.'
                }
                return responseObject, 200
            return {"message": save_in_blacklist.get_error(), "status": "fail"}, 401
        responseObject = {
            'status': 'fail',
            'message': resp
        }
        return responseObject, 401
