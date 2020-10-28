
class Cliente:
    def __init__(
        self, id_cliente, nome, pregao, processo_compras,
        contrato, linha, departamento_contato, fone, contato, email,
        cpf, cnpj, inscricao_estadual, inscricao_municipal,
        logradouro, numero, bairro, cidade, estado, cep
    ):
        self._id = id_cliente
        self._nome = nome
        self._pregao = pregao
        self._processo_compras = processo_compras
        self._contrato = contrato
        self._linha = linha
        self._departamento_contato = departamento_contato
        self._fone = fone
        self._contato = contato
        self._email = email
        self._cpf = cpf
        self._cnpj = cnpj
        self._inscricao_estadual = inscricao_estadual
        self._inscricao_municipal = inscricao_municipal
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep
