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


class MultaDAO():
    def __init__(self):
        self._errorMsg = None

    def list_multa(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Mul.*, Ve.renavam, Ve.placa,\
        concat(Col.nome,' ',Col.sobrenome) AS colaborador\
        FROM multa AS Mul\
            LEFT JOIN veiculo AS Ve\
            ON Mul.veiculo_id = Ve.id\
            LEFT JOIN colaborador as Col\
            ON Mul.colaborador_id = Col.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        lista_multa = decimal_to_float.default(dados)
        multa = self.update_date_time(lista_multa)
        dicio = {"items": multa}
        return dicio

    def find_multa(self, id_multa):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Mul.*, Ve.renavam, Ve.placa,\
        concat(Col.nome,' ',Col.sobrenome) AS colaborador\
        FROM multa AS Mul\
            LEFT JOIN veiculo AS Ve\
            ON Mul.veiculo_id = Ve.id\
            LEFT JOIN colaborador as Col\
            ON Mul.colaborador_id = Col.id\
        WHERE Mul.id = %s "
        valor = (id_multa,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        multa = decimal_to_float.default(dados)
        if len(multa) > 0:
            multa[0]["hora"] = str(multa[0]["hora"])
        return multa[0]

    def save_multa(self, multa):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO multa(\
        id,\
        codigo_ait,\
        data,\
        hora,\
        local,\
        descricao,\
        valor, \
        status,\
        veiculo_id,\
        colaborador_id)\
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (
            multa._id, multa._codigo_ait, multa._data,
            multa._hora, multa._local, multa._descricao,
            multa._valor, multa._status, multa._veiculo_id,
            multa._colaborador_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_multa(self, multa):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE multa SET\
        codigo_ait = %s,\
        data = %s,\
        hora = %s,\
        local = %s,\
        descricao = %s,\
        valor = %s, \
        status = %s,\
        veiculo_id = %s,\
        colaborador_id = %s\
        WHERE id = %s"
        valor = multa._id
        dados = (
            multa._codigo_ait, multa._data,
            multa._hora, multa._local, multa._descricao,
            multa._valor, multa._status, multa._veiculo_id,
            multa._colaborador_id, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_multa(self, id_multa):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM multa WHERE id = %s"
        valor = (id_multa,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg

    def update_date_time(self, multa):
        for dicio in multa:
            if "hora" in dicio:
                dicio["hora"] = str(dicio["hora"])
        return multa


class DecimalEncoder:
    def default(self, list_dicio):
        for dicio in list_dicio:
            for key, valor in dicio.items():
                if isinstance(valor, D):
                    dicio[key] = float(valor)
        return list_dicio
