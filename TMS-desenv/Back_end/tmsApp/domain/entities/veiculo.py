class Veiculo:
    def __init__(
        self, id_veiculo, marca, placa, ano, renavam, 
        mes_licenciamento, vencimento_ipva, status, 
        valor_ipva, valor_licenciamento, valor_dpvat
    ):
        self._id = id_veiculo
        self._marca = marca
        self._placa = placa
        self._ano = ano
        self._renavam = renavam
        self._mes_licenciamento = mes_licenciamento
        self._vencimento_ipva = vencimento_ipva
        self._status = status
        self._valor_ipva = valor_ipva
        self._valor_licenciamento = valor_licenciamento
        self._valor_dpvat = valor_dpvat
