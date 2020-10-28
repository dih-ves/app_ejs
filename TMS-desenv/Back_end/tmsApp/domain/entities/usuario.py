import jwt
import datetime
import tmsApp.main as tmsMain
import tmsApp.domain.repository.blacklistTokendao as blacklist

app = tmsMain.app


class Usuario:
    def __init__(
        self, id_usuario, user_name, nome, sobrenome,
        email, senha, cargo_id, departamento_id, grupo_id
    ):
        self._id = id_usuario
        self._user_name = user_name
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
        self._senha = senha
        self._cargo_id = cargo_id
        self._departamento_id = departamento_id
        self._grupo_id = grupo_id
        self._errorMsg = None

    def encode_auth_token(self, user_id):
        '''
        gera o Auth Token
        :return: string
        exp: data de expiracao do token
        iat: a hora/time que o token foi gerado
        sub: o subject do token (o usuario quem ele identifica)
        '''
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=60),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id,
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            self._errorMsg = str(e)
            return None

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            blacklistToken = blacklist.BlacklistTokenDAO()
            token_em_blacklist = blacklistToken.check_blacklistToken(auth_token)
            if token_em_blacklist:
                return "Senha expirada. Realize um novo login."
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Senha expirada. Realize um novo login.'
        except jwt.InvalidTokenError:
            return 'token Invalido. Realize um novo login.'

    def get_error(self):
        return self._errorMsg
