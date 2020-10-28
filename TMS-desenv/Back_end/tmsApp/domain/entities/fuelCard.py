class FuelCard:
    def __init__(
        self, id_cartao, numero, tipo, senha, unidade,
        status, fornecedor_id, veiculo_id, colaborador_id
    ):
        self._id = id_cartao
        self._numero = numero
        self._tipo = tipo
        self._senha = senha
        self._unidade = unidade
        self._status = status
        self._fornecedor_id = fornecedor_id
        self._veiculo_id = veiculo_id
        self._colaborador_id = colaborador_id
