import mysql.connector as mysql


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class RdvoDAO():
    def __init__(self):
        self._errorMsg = None

    def list_rdvo(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Rd.*, day(inicio_viagem) as dia, monthname(inicio_viagem) as mes,\
        YEAR(inicio_viagem) as Ano,\
        Rd.hodometro_fim-Rd.hodometro_ini as km_rodado_mes,\
        Cli.nome as cliente\
        FROM rdvo AS Rd\
            LEFT JOIN cliente AS Cli\
            ON Rd.cliente_id = Cli.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def list_intervalo_rdvo(self, ano, mes):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Rd.*, day(inicio_viagem) as dia, monthname(inicio_viagem) as mes,\
        YEAR(inicio_viagem) as Ano,\
        Rd.hodometro_fim-Rd.hodometro_ini as km_rodado_mes,\
        Cli.nome as cliente\
        FROM rdvo AS Rd\
            LEFT JOIN cliente AS Cli\
            ON Rd.cliente_id = Cli.id\
        WHERE YEAR(inicio_viagem) = %s AND MONTH(inicio_viagem) = %s"
        valor = (ano, mes)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_rdvo(self, id_rdvo):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Rd.*, day(inicio_viagem) as dia, month(inicio_viagem) as mes,\
        YEAR(inicio_viagem) as Ano,\
        Rd.hodometro_fim-Rd.hodometro_ini as km_rodado_mes,\
        Cli.nome as cliente\
        FROM rdvo AS Rd\
            LEFT JOIN cliente AS Cli\
            ON Rd.cliente_id = Cli.id\
        WHERE Rd.id = %s "
        valor = (id_rdvo,)
        cursor.execute(sqlQuery, valor)
        rdvo = cursor.fetchall()
        if rdvo is None or rdvo == []:
            return None
        return rdvo[0]

    def save_rdvo(self, rdvo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO rdvo(\
        id,\
        posto,\
        ltu,\
        inicio_viagem,\
        hodometro_ini,\
        hodometro_fim,\
        cliente_id)\
        VALUES(%s, %s, %s, %s, %s, %s, %s)"
        dados = (
            rdvo._id, rdvo._posto, rdvo._ltu, rdvo._inicio_viagem,
            rdvo._hodometro_ini, rdvo._hodometro_fim, rdvo._cliente_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_rdvo(self, rdvo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE rdvo SET\
        posto = %s,\
        ltu = %s,\
        inicio_viagem = %s,\
        hodometro_ini = %s,\
        hodometro_fim = %s,\
        cliente_id = %s\
        WHERE id  = %s"
        valor = rdvo._id
        dados = (
            rdvo._posto, rdvo._ltu, rdvo._inicio_viagem,
            rdvo._hodometro_ini, rdvo._hodometro_fim,
            rdvo._cliente_id, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_rdvo(self, id_rdvo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM rdvo WHERE id = %s"
        valor = (id_rdvo,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
