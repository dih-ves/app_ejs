import mysql.connector as mysql


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class GrupoDAO():
    def __init__(self):
        self._errorMsg = None

    def list_grupo(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * from grupo"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_grupo(self, id_grupo):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * FROM grupo WHERE id = %s "
        valor = (id_grupo,)
        cursor.execute(sqlQuery, valor)
        grupo = cursor.fetchall()
        if grupo is None or grupo == []:
            return None
        return grupo[0]

    def save_grupo(self, grupo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO grupo(id, nome) VALUES(%s, %s)"
        dados = (grupo._id, grupo._nome)
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_grupo(self, grupo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE grupo SET nome = %s WHERE id  = %s"
        valor = grupo._id
        dados = (grupo._nome, valor)
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_grupo(self, id_grupo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM grupo WHERE id = %s"
        valor = (id_grupo,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
