# Classe do Registro de Manutenção de Veículos
class Manutencao:
    def __init__(
        self, id_manutencao, veiculo_id, colaborador_id,
        data_inicial, data_final
    ):
        self._id = id_manutencao
        self._veiculo_id = veiculo_id
        self._colaborador_id = colaborador_id
        self._data_inicial = data_inicial
        self._data_final = data_final
