# Classe de Controle de Colaboradores
class ControlColab:
    def __init__(
        self, id_control, colaborador_id, ano, mes, cartao_ponto,
        recibo_vr, recibo_vt
    ):
        self._id = id_control
        self._colaborador_id = colaborador_id
        self._ano = ano
        self._mes = mes
        self._cartao_ponto = cartao_ponto
        self._recibo_vr = recibo_vr
        self._recibo_vt = recibo_vt
