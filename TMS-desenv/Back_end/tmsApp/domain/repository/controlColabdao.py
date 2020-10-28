import mysql.connector as mysql
from decimal import Decimal as D


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class ControlColabDAO():
    def __init__(self):
        self._errorMsg = None

    def list_controlColab(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Con.*, Dd.*,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        Ve.placa\
        from controleColaborador AS Con\
            LEFT JOIN ddsp as Dd\
            ON Con.colaborador_id = Dd.colaborador_id\
            LEFT JOIN colaborador AS Col\
            ON Con.colaborador_id = Col.id\
            LEFT JOIN veiculo AS Ve\
            ON Dd.veiculo_id = Ve.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        ctrlColab = decimal_to_float.default(dados)
        res = self.update_date_time(ctrlColab)
        dicio = {"items": res}
        return dicio

    def find_controlColab(self, id_control):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Con.*, Dd.*,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        Ve.placa\
        from controleColaborador AS Con\
            LEFT JOIN ddsp as Dd\
            ON Con.colaborador_id = Dd.colaborador_id\
            LEFT JOIN colaborador AS Col\
            ON Con.colaborador_id = Col.id\
            LEFT JOIN veiculo AS Ve\
            ON Dd.veiculo_id = Ve.id\
        WHERE Con.id = %s "
        valor = (id_control,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        ctrlColab = decimal_to_float.default(dados)
        res = self.update_date_time(ctrlColab)
        return res[0]

    def find_controlColab_by_Colab_id(self, colaborador_id):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Con.*, Dd.*,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        Ve.placa\
        from controleColaborador AS Con\
            LEFT JOIN ddsp as Dd\
            ON Con.colaborador_id = Dd.colaborador_id\
            LEFT JOIN colaborador AS Col\
            ON Con.colaborador_id = Col.id\
            LEFT JOIN veiculo AS Ve\
            ON Dd.veiculo_id = Ve.id\
        WHERE Col.id = %s "
        valor = (colaborador_id,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        ctrlColab = decimal_to_float.default(dados)
        res = self.update_date_time(ctrlColab)
        return res[0]

    def save_controlColab(self, controlColab):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO controleColaborador(\
        id,\
        colaborador_id,\
        ano,\
        mes,\
        cartao_ponto,\
        recibo_vr,\
        recibo_vt)\
        VALUES(%s, %s, %s, %s, %s, %s, %s)"
        dados = (
            controlColab._id, controlColab._colaborador_id,
            controlColab._ano, controlColab._mes,
            controlColab._cartao_ponto, controlColab._recibo_vr,
            controlColab._recibo_vt
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_controlColab(self, controlColab):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE controleColaborador SET\
        colaborador_id = %s,\
        ano = %s,\
        mes = %s,\
        cartao_ponto = %s,\
        recibo_vr = %s,\
        recibo_vt = %s\
        WHERE id  = %s"
        valor = (controlColab._id)
        dados = (
            controlColab._colaborador_id,
            controlColab._ano, controlColab._mes,
            controlColab._cartao_ponto, controlColab._recibo_vr,
            controlColab._recibo_vt, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_controlColab(self, id_control):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM controleColaborador WHERE id = %s"
        valor = (id_control,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg

    def update_date_time(self, ctrlColab):
        for dicio in ctrlColab:
            if "horario_ini" in dicio:
                dicio["horario_ini"] = str(dicio["horario_ini"])
            if "horario_fim" in dicio:
                dicio["horario_fim"] = str(dicio["horario_fim"])
        return ctrlColab


class DecimalEncoder:
    def default(self, list_dicio):
        for dicio in list_dicio:
            for key, valor in dicio.items():
                if isinstance(valor, D):
                    dicio[key] = float(valor)
        return list_dicio
