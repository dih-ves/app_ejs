import mysql.connector as mysql
# script nao esta sendo utilizado, item gravado e atualizado juntamente
# com a manutencaoVeiculo


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class ItemManutencaoDAO():
    def __init__(self):
        self._errorMsg = None

    def list_itemManutencao(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * from itemManutencao"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        itemMan = decimal_to_float.default(dados)
        dicio = {"items": itemMan}
        return dicio

    def find_itemManutencao(self, id_itemManutencao):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT * FROM itemManutencao WHERE id = %s "
        valor = (id_itemManutencao,)
        cursor.execute(sqlQuery, valor)
        itemManutencao = cursor.fetchall()
        if itemManutencao is None or itemManutencao == []:
            return None
        decimal_to_float = DecimalEncoder()
        itemMan = decimal_to_float.default(dados)
        return itemMan[0]

    def save_itemManutencao(self, itemManutencao):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO itemManutencao(\
        id,\
        tipo,\
        nome,\
        preco,\
        fornecedor_id,\
        manutencaoVeiculo_id)\
        VALUES(%s, %s, %s, %s, %s, %s)"
        dados = (
            itemManutencao._id, itemManutencao._tipo, itemManutencao._nome,
            itemManutencao._preco, itemManutencao._fornecedor_id,
            itemManutencao._manutencaoVeiculo_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_itemManutencao(self, itemManutencao):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE itemManutencao SET\
        tipo = %s,\
        nome = %s,\
        preco = %s,\
        fornecedor_id = %s,\
        manutencaoVeiculo_id = %s\
        WHERE id  = %s"
        valor = itemManutencao._id
        dados = (
            itemManutencao._tipo, itemManutencao._nome,
            itemManutencao._preco, itemManutencao._fornecedor_id,
            itemManutencao._manutencaoVeiculo_id, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_itemManutencao(self, id_itemManutencao):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM itemManutencao WHERE id = %s"
        valor = (id_itemManutencao,)
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