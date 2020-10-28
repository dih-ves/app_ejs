import mysql.connector as mysql


# cria a conexao com o banco
def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class ColaboradorDAO():
    def __init__(self):
        self._errorMsg = None

    def list_colaborador(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Co.*, Dep.nome AS departamento,\
        Ca.nome AS cargo, Gp.nome As grupo\
        FROM colaborador AS Co\
            LEFT JOIN departamento AS Dep\
            ON Co.departamento_id = Dep.id\
            LEFT JOIN cargo AS Ca\
            ON Co.cargo_id = Ca.id\
            LEFT JOIN grupo as Gp\
            ON Co.grupo_id = gp.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        if len(dados) > 1:
            return dados
        dicio = {"items": dados}
        return dicio

    def find_colaborador(self, id_colaborador):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Co.*, Dep.nome AS departamento,\
        Ca.nome AS cargo, Gp.nome As grupo\
        FROM colaborador AS Co\
            LEFT JOIN departamento AS Dep\
            ON Co.departamento_id = Dep.id\
            LEFT JOIN cargo AS Ca\
            ON Co.cargo_id = Ca.id\
            LEFT JOIN grupo as Gp\
            ON Co.grupo_id = gp.id\
        WHERE Co.id = %s "
        valor = (id_colaborador,)
        cursor.execute(sqlQuery, valor)
        colaborador = cursor.fetchall()
        if colaborador is None or colaborador == []:
            return None
        if len(colaborador) > 1:
            return colaborador
        return colaborador[0]

    def save_colaborador(self, colaborador):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "Insert INTO colaborador(\
        id,\
        nome,\
        sobrenome,\
        admissao,\
        fone,\
        ctps,\
        rg,\
        cpf,\
        cnh,\
        categoria,\
        logradouro,\
        numero,\
        bairro,\
        cidade,\
        estado,\
        cep,\
        demissao,\
        departamento_id,\
        cargo_id,\
        grupo_id)\
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (
            colaborador._id, colaborador._nome, colaborador._sobrenome,
            colaborador._admissao, colaborador._fone,
            colaborador._ctps, colaborador._rg, colaborador._cpf,
            colaborador._cnh, colaborador._categoria,
            colaborador._logradouro, colaborador._numero,
            colaborador._bairro, colaborador._cidade,
            colaborador._estado, colaborador._cep,
            colaborador._demissao,
            colaborador._departamento_id, colaborador._cargo_id,
            colaborador._grupo_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_colaborador(self, colaborador):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE colaborador SET\
        nome = %s,\
        sobrenome = %s,\
        admissao = %s,\
        fone = %s,\
        ctps = %s,\
        rg = %s,\
        cpf = %s,\
        cnh = %s,\
        categoria = %s,\
        logradouro = %s,\
        numero = %s,\
        bairro = %s,\
        cidade = %s,\
        estado = %s,\
        cep = %s,\
        demissao = %s\
        departamento_id = %s,\
        cargo_id = %s,\
        grupo_id = %s\
        WHERE id = %s"
        valor = colaborador._id
        dados = (
            colaborador._nome, colaborador._sobrenome,
            colaborador._admissao, colaborador._fone,
            colaborador._ctps, colaborador._rg, colaborador._cpf,
            colaborador._cnh, colaborador._categoria,
            colaborador._logradouro, colaborador._numero,
            colaborador._bairro, colaborador._cidade,
            colaborador._estado, colaborador._cep,
            colaborador._demissao,
            colaborador._departamento_id, colaborador._cargo_id,
            colaborador._grupo_id, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_colaborador(self, id_colaborador):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM colaborador WHERE id = %s"
        valor = (id_colaborador,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
