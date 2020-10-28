class Multa:
    def __init__(
        self, id_multa, codigo_ait, data,
        hora, local, descricao, valor, status, veiculo_id,
        colaborador_id
    ):
        self._id = id_multa
        self._codigo_ait = codigo_ait
        self._data = data
        self._hora = hora
        self._local = local
        self._descricao = descricao
        self._valor = valor
        self._status = status
        self._veiculo_id = veiculo_id
        self._colaborador_id = colaborador_id
