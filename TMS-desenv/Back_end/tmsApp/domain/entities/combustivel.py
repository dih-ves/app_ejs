# Classe de Registro de Consumo de Combustível
class Combustivel:
    def __init__(
        self, id_combustivel, data, litro, preco,
        veiculo_id, colaborador_id, fornecedor_id
    ):
        self._id = id_combustivel
        self._data = data
        self._litro = litro
        self._preco = preco
        self._veiculo_id = veiculo_id
        self._colaborador_id = colaborador_id
        self._fornecedor_id = fornecedor_id
