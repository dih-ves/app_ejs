
class Colaborador:
    def __init__(
        self, id_colaborador, nome, sobrenome,
        admissao, fone, departamento_id, cargo_id,
        ctps, rg, cpf, cnh, categoria, logradouro,
        numero, bairro, cidade, estado, cep, demissao, grupo_id
    ):
        self._id = id_colaborador
        self._nome = nome
        self._sobrenome = sobrenome
        self._admissao = admissao
        self._fone = fone
        self._departamento_id = departamento_id
        self._cargo_id = cargo_id
        self._ctps = ctps
        self._rg = rg
        self._cpf = cpf
        self._cnh = cnh
        self._categoria = categoria
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep
        self._demissao = demissao
        self._grupo_id = grupo_id
