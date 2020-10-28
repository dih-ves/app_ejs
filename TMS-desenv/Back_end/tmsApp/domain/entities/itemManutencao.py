class ItemManutencao:
    def __init__(
        self, id_manutencao, id_itemManutencao, tipo, nome, preco,
        fornecedor_id
    ):
        self._manutencaoVeiculo_id = id_manutencao
        self._id = id_itemManutencao
        self._tipo = tipo
        self._nome = nome
        self._preco = preco
        self._fornecedor_id = fornecedor_id
