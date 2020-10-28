class Fornecedor:
    def __init__(
        self, id_fornecedor, nome, nome_fantasia, tipo_produto,
        cnpj, inscricao_estadual, inscricao_municipal,
        fone, contato, email, departamento_contato,
        logradouro, numero, bairro, cidade, estado, cep
    ):
        self._id = id_fornecedor
        self._nome = nome
        self._nome_fantasia = nome_fantasia
        self._tipo_produto = tipo_produto
        self._cnpj = cnpj
        self._inscricao_estadual = inscricao_estadual
        self._inscricao_municipal = inscricao_municipal
        self._fone = fone
        self._contato = contato
        self._email = email
        self._departamento_contato = departamento_contato
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep
