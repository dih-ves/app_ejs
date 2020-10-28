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


class FornecedorDAO:
    def __init__(self):
        self._errorMsg = None

    def list_fornecedor(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT F.*, D.nome as departamento\
        FROM fornecedor as F\
            LEFT JOIN departamento as D\
            ON D.id = F.departamento_id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_fornecedor(self, id_fornecedor):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT F.*, D.nome as departamento\
        FROM fornecedor as F\
            LEFT JOIN departamento as D\
            ON D.id = F.departamento_id\
        WHERE F.id = %s "
        valor = (id_fornecedor,)
        cursor.execute(sqlQuery, valor)
        fornecedor = cursor.fetchall()
        if fornecedor is None or fornecedor == []:
            return None
        return fornecedor[0]

    def save_fornecedor(self, fornecedor):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO fornecedor (\
        id,\
        nome,\
        nome_fantasia,\
        tipo_produto,\
        cnpj,\
        inscricao_estadual,\
        inscricao_municipal,\
        fone,\
        contato,\
        email,\
        departamento_contato,\
        logradouro,\
        numero,\
        bairro,\
        cidade,\
        estado,\
        cep)\
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,\
        %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (
            fornecedor._id, fornecedor._nome, fornecedor._nome_fantasia,
            fornecedor._tipo_produto, fornecedor._cnpj,
            fornecedor._inscricao_estadual, fornecedor._inscricao_municipal,
            fornecedor._fone, fornecedor._contato, fornecedor._email,
            fornecedor._departamento_contato, fornecedor._logradouro,
            fornecedor._numero, fornecedor._bairro, fornecedor._cidade,
            fornecedor._estado, fornecedor._cep
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_fornecedor(self, fornecedor):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE fornecedor SET\
        nome = %s,\
        nome_fantasia = %s,\
        tipo_produto = %s,\
        cnpj = %s,\
        inscricao_estadual = %s,\
        inscricao_municipal = %s,\
        fone = %s,\
        contato = %s,\
        email = %s,\
        departamento_contato = %s,\
        logradouro = %s,\
        numero = %s,\
        bairro = %s,\
        cidade = %s,\
        estado = %s,\
        cep = %s\
        WHERE id = %s"
        valor = fornecedor._id
        dados = (
            fornecedor._nome, fornecedor._nome_fantasia,
            fornecedor._tipo_produto, fornecedor._cnpj,
            fornecedor._inscricao_estadual, fornecedor._inscricao_municipal,
            fornecedor._fone, fornecedor._contato, fornecedor._email,
            fornecedor._departamento_contato, fornecedor._logradouro,
            fornecedor._numero, fornecedor._bairro, fornecedor._cidade,
            fornecedor._estado, fornecedor._cep, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_fornecedor(self, id_fornecedor):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM fornecedor WHERE id = %s"
        valor = (id_fornecedor,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
