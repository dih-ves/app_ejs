# Classe do Demonstrativo Diário de Serviços Prestados -> DDSP
class DemDiario:
    def __init__(
        self, id_dem, data, hodometro_ini,
        hodometro_fim, horario_ini, horario_fim,
        intervalo_ini, intervalo_fim, usuario_sr,
        valor_hora, colaborador_id, veiculo_id
    ):
        self._id = id_dem
        self._data = data
        self._hodometro_ini = hodometro_ini
        self._hodometro_fim = hodometro_fim
        self._horario_ini = horario_ini
        self._horario_fim = horario_fim
        self._intervalo_ini = intervalo_ini
        self._intervalo_fim = intervalo_fim
        self._usuario_sr = usuario_sr
        self._valor_hora = valor_hora
        self._colaborador_id = colaborador_id
        self._veiculo_id = veiculo_id
