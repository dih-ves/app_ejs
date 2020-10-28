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


class ClienteDAO():
    def __init__(self):
        self._errorMsg = None

    def list_cliente(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT cl.*, Dep.nome as departamento from cliente as cl\
        LEFT JOIN departamento as Dep\
        ON cl.departamento_id = Dep.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        dicio = {"items": dados}
        return dicio

    def find_cliente(self, id_cliente):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT cl.*, Dep.nome as departamento from cliente as cl\
            LEFT JOIN departamento as Dep\
            ON cl.departamento_id = Dep.id\
        WHERE cl.id = %s "
        valor = (id_cliente,)
        cursor.execute(sqlQuery, valor)
        cliente = cursor.fetchall()
        if cliente is None or cliente == []:
            return None
        return cliente[0]

    def save_cliente(self, cliente):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "Insert INTO cliente(\
            id,\
            nome,\
            pregao,\
            processo_compras,\
            contrato,\
            linha,\
            contato,\
            fone,\
            departamento_contato,\
            email,\
            cpf,\
            cnpj,\
            inscricao_estadual,\
            inscricao_municipal,\
            logradouro,\
            numero,\
            bairro,\
            cidade,\
            estado,\
            cep)\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,\
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (
            cliente._id, cliente._nome, cliente._pregao,
            cliente._processo_compras, cliente._contrato, cliente._linha,
            cliente._contato, cliente._fone, cliente._departamento_contato,
            cliente._email, cliente._cpf, cliente._cnpj,
            cliente._inscricao_estadual, cliente._inscricao_municipal,
            cliente._logradouro, cliente._numero, cliente._bairro,
            cliente._cidade, cliente._estado, cliente._cep
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_cliente(self, cliente):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE cliente SET\
        nome = %s,\
        pregao = %s,\
        processo_compras = %s,\
        contrato = %s,\
        linha = %s,\
        contato = %s,\
        fone = %s,\
        departamento_contato = %s,\
        email = %s,\
        cpf = %s,\
        cnpj = %s,\
        inscricao_estadual = %s,\
        inscricao_municipal = %s,\
        logradouro = %s,\
        numero = %s,\
        bairro = %s,\
        cidade = %s,\
        estado = %s,\
        cep = %s\
        WHERE id = %s"
        valor = cliente._id
        dados = (
            cliente._nome, cliente._pregao,
            cliente._processo_compras, cliente._contrato, cliente._linha,
            cliente._contato, cliente._fone, cliente._departamento_contato,
            cliente._email, cliente._cpf, cliente._cnpj,
            cliente._inscricao_estadual, cliente._inscricao_municipal,
            cliente._logradouro, cliente._numero, cliente._bairro,
            cliente._cidade, cliente._estado, cliente._cep, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_cliente(self, id_cliente):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM cliente WHERE id = %s"
        valor = (id_cliente,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg
