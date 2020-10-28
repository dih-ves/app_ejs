import mysql.connector as mysql


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class UsuarioDAO():
    def __init__(self):
        self._errorMsg = None

    def find_usuarios(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Us.id, Us.nome, Us.sobrenome, Us.user_name, Us.email,\
        Dep.nome as departamento, Car.nome as cargo, Gp.nome as grupo\
        FROM usuario AS Us\
            LEFT JOIN departamento AS Dep\
            ON Us.departamento_id = Dep.id\
            LEFT JOIN cargo As Car\
            ON Us.cargo_id = Car.id\
            LEFT JOIN grupo as Gp\
            ON Us.grupo_id = Gp.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_usuario(self, id_usuario):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Us.id, Us.nome, Us.sobrenome, Us.user_name, Us.email,\
        Dep.nome as departamento, Car.nome as cargo, Gp.nome as grupo\
        FROM usuario AS Us\
            LEFT JOIN departamento AS Dep\
            ON Us.departamento_id = Dep.id\
            LEFT JOIN cargo As Car\
            ON Us.cargo_id = Car.id\
            LEFT JOIN grupo as Gp\
            ON Us.grupo_id = Gp.id\
        WHERE Us.id = %s"
        valor = (id_usuario,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        return dados[0]

    def find_usuario_to_auth(self, user_name):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT Us.*, Gp.nome FROM usuario as Us\
            LEFT JOIN grupo as Gp\
            ON Us.grupo_id = Gp.id\
        WHERE user_name = %s or email = %s"
        valor = (user_name, user_name)
        cursor.execute(sqlQuery, valor)
        usuario = cursor.fetchall()
        if usuario is None or usuario == []:
            return None
        return usuario[0]

    def save_usuario(self, usuario):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO usuario(\
        id,\
        user_name,\
        nome,\
        sobrenome,\
        email,\
        senha,\
        cargo_id,\
        departamento_id,\
        grupo_id)\
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (
            usuario._id,  usuario._user_name, usuario._nome,
            usuario._sobrenome, usuario._email, usuario._senha,
            usuario._cargo_id, usuario._departamento_id, usuario._grupo_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_usuario(self, usuario):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE usuario SET\
        user_name = %s,\
        nome = %s,\
        sobrenome = %s,\
        email = %s,\
        senha = %s,\
        cargo_id = %s,\
        departamento_id = %s,\
        grupo_id = %s\
        WHERE id = %s"
        valor = usuario._id
        dados = (
            usuario._user_name, usuario._nome,
            usuario._sobrenome, usuario._email, usuario._senha,
            usuario._cargo_id, usuario._departamento_id, usuario._grupo_id,
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

    def delete_usuario(self, id_usuario):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM usuario WHERE id = %s"
        valor = (id_usuario,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
