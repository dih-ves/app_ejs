import mysql.connector as mysql


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class FuelCardDAO():
    def __init__(self):
        self._errorMsg = None

    def list_fuelCard(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Car.*, Fo.nome as fornecedor,\
        Ve.placa, concat(Col.nome,' ',Col.sobrenome) as colaborador\
        FROM cartaoCombustivel AS Car\
            LEFT JOIN fornecedor AS Fo\
            ON Car.fornecedor_id = Fo.id\
            LEFT JOIN veiculo AS Ve\
            ON Car.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Car.colaborador_id = Col.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_fuelCard(self, id_cartao):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Car.*, Fo.nome as fornecedor,\
        Ve.placa, concat(Col.nome,' ',Col.sobrenome) as colaborador\
        FROM cartaoCombustivel AS Car\
            LEFT JOIN fornecedor AS Fo\
            ON Car.fornecedor_id = Fo.id\
            LEFT JOIN veiculo AS Ve\
            ON Car.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Car.colaborador_id = Col.id\
        WHERE Car.id = %s "
        valor = (id_cartao,)
        cursor.execute(sqlQuery, valor)
        fuelCard = cursor.fetchall()
        if fuelCard is None or fuelCard == []:
            return None
        return fuelCard[0]

    def save_fuelCard(self, fuelCard):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO cartaoCombustivel(\
        id,\
        numero,\
        tipo,\
        senha,\
        unidade,\
        status,\
        fornecedor_id,\
        veiculo_id,\
        colaborador_id)\
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (
            fuelCard._id, fuelCard._numero,
            fuelCard._tipo, fuelCard._senha,
            fuelCard._unidade, fuelCard._status,
            fuelCard._fornecedor_id, fuelCard._veiculo_id,
            fuelCard._colaborador_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_fuelCard(self, fuelCard):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE cartaoCombustivel SET\
        numero = %s,\
        tipo = %s,\
        senha = %s,\
        unidade = %s,\
        status = %s,\
        fornecedor_id = %s,\
        veiculo_id = %s,\
        colaborador_id = %s\
        WHERE id = %s"
        valor = fuelCard._id
        dados = (
            fuelCard._numero,
            fuelCard._tipo, fuelCard._senha,
            fuelCard._unidade, fuelCard._status,
            fuelCard._fornecedor_id, fuelCard._veiculo_id,
            fuelCard._colaborador_id, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_fuelCard(self, id_cartao):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM cartaoCombustivel WHERE id = %s"
        valor = (id_cartao,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
