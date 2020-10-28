import mysql.connector as mysql


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class CargoDAO():
    def __init__(self):
        self._errorMsg = None

    def list_cargo(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * from cargo"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_cargo(self, id_cargo):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * FROM cargo WHERE id = %s "
        valor = (id_cargo,)
        cursor.execute(sqlQuery, valor)
        cargo = cursor.fetchall()
        if cargo is None or cargo == []:
            return None
        return cargo[0]

    def save_cargo(self, cargo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO cargo(id, nome) VALUES(%s, %s)"
        dados = (cargo._id, cargo._nome)
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_cargo(self, cargo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE cargo SET nome = %s WHERE id  = %s"
        valor = cargo._id
        dados = (cargo._nome, valor)
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_cargo(self, id_cargo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM cargo WHERE id = %s"
        valor = (id_cargo,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
