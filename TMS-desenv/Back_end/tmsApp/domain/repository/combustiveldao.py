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


class CombustivelDAO():
    def __init__(self):
        self._errorMsg = None

    def list_combustivel(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Com.*, format(Com.litro*Com.preco, 2) as total, Ve.placa,\
        concat(Col.nome,' ',Col.sobrenome) AS colaborador,\
        Fo.nome AS fornecedor\
        FROM combustivel AS Com\
            LEFT JOIN veiculo AS Ve\
            ON Com.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Com.colaborador_id = Col.id\
            LEFT JOIN fornecedor AS Fo\
            ON Com.fornecedor_id = Fo.id"
        # query para retorno de media mensal de consumo
        sqlQuery2 = "SELECT monthname(data) as mes, round(avg(preco), 2)\
        AS 'media_de_preco', round(avg(litro), 2) AS 'litros'\
        FROM combustivel\
        GROUP BY mes"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        cursor.execute(sqlQuery2)
        dados2 = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        combustivel = decimal_to_float.default(dados)
        media = decimal_to_float.default(dados2)
        dicio = {"items": combustivel, "media_mensal": media}
        return dicio

    def list_intervalo_combustivel(self, ano, mes):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Com.*, Com.litro*Com.preco as total, Ve.placa,\
        concat(Col.nome,' ',Col.sobrenome) AS colaborador,\
        Fo.nome AS fornecedor\
        FROM combustivel AS Com\
            LEFT JOIN veiculo AS Ve\
            ON Com.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Com.colaborador_id = Col.id\
            LEFT JOIN fornecedor AS Fo\
            ON Com.fornecedor_id = Fo.id\
        WHERE YEAR(Com.data) = %s and MONTH(Com.data) = %s"
        # query para retorno de media mensal de consumo
        sqlQuery2 = "SELECT round(avg(preco), 2) AS 'media_de_preco', round(avg(litro), 2) AS 'litros'\
        FROM combustivel\
        WHERE YEAR(data) = %s and MONTH(data) = %s"
        valor = (ano, mes)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        cursor.execute(sqlQuery2, valor)
        dados2 = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        combustivel = decimal_to_float.default(dados)
        media = decimal_to_float.default(dados2)
        dicio = {"items": combustivel, "media_mensal": media}
        return dicio

    def find_combustivel(self, id_combustivel):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Com.*, Com.litro*Com.preco as total, Ve.placa,\
        concat(Col.nome,' ',Col.sobrenome) AS colaborador,\
        Fo.nome AS fornecedor\
        FROM combustivel AS Com\
            LEFT JOIN veiculo AS Ve\
            ON Com.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Com.colaborador_id = Col.id\
            LEFT JOIN fornecedor AS Fo\
            ON Com.fornecedor_id = Fo.id\
        WHERE Com.id = %s"
        valor = (id_combustivel,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        combustivel = decimal_to_float.default(dados)
        dicio = {"items": combustivel}
        return dicio

    def save_combustivel(self, combustivel):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO combustivel(\
        id,\
        data,\
        litro,\
        preco,\
        veiculo_id,\
        colaborador_id,\
        fornecedor_id)\
        VALUES(%s, %s, %s, %s, %s, %s, %s)"
        dados = (
            combustivel._id, combustivel._data, combustivel._litro,
            combustivel._preco, combustivel._veiculo_id,
            combustivel._colaborador_id, combustivel._fornecedor_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_combustivel(self, combustivel):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE combustivel SET\
        data = %s,\
        litro = %s,\
        preco = %s,\
        veiculo_id = %s,\
        colaborador_id = %s,\
        fornecedor_id = %s\
        WHERE id  = %s"
        valor = combustivel._id
        dados = (
            combustivel._data, combustivel._litro,
            combustivel._preco, combustivel._veiculo_id,
            combustivel._colaborador_id, combustivel._fornecedor_id,
            valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_combustivel(self, id_combustivel):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM combustivel WHERE id = %s"
        valor = (id_combustivel,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg


class DecimalEncoder:
    def default(self, list_dicio):
        for dicio in list_dicio:
            for key, valor in dicio.items():
                if isinstance(valor, D):
                    dicio[key] = float(valor)
        return list_dicio
