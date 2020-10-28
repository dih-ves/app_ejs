import mysql.connector as mysql


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class DepartamentoDAO():
    def __init__(self):
        self._errorMsg = None

    def list_departamento(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * from departamento"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_departamento(self, id_departamento):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * FROM departamento WHERE id = %s "
        valor = (id_departamento,)
        cursor.execute(sqlQuery, valor)
        departamento = cursor.fetchall()
        if departamento is None or departamento == []:
            return None
        return departamento[0]

    def save_departamento(self, departamento):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO departamento(id, nome) VALUES(%s, %s)"
        dados = (departamento._id, departamento._nome)
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_departamento(self, departamento):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE departamento SET nome = %s WHERE id  = %s"
        valor = departamento._id
        dados = (departamento._nome, valor)
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_departamento(self, id_departamento):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM departamento WHERE id = %s"
        valor = (id_departamento,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
