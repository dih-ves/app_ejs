# Classe do Registro Diário de Viagens e Ocorrências
class Rdvo:
    def __init__(
        self, id_rdvo, posto, ltu, inicio_viagem,
        hodometro_ini, hodometro_fim, cliente_id
    ):
        self._id = id_rdvo
        self._posto = posto
        self._ltu = ltu
        self._inicio_viagem = inicio_viagem
        self._hodometro_ini = hodometro_ini
        self._hodometro_fim = hodometro_fim
        self._cliente_id = cliente_id
