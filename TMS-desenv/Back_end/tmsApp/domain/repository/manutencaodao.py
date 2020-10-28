import mysql.connector as mysql
import json
from decimal import Decimal as D


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class ManutencaoDAO():
    def __init__(self):
        self._errorMsg = None

    def list_manutencao(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Mv.*,Mv.id as id_manutencao, Im.*, Fo.nome as fornecedor, Ve.placa,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        monthname(Mv.data_inicial) as mes,\
        ifnull((select sum(preco) from itemManutencao where manutencaoVeiculo_id = Mv.id), 0) as total_itens,\
        ifnull((select sum(preco) from itemManutencao), 0) as total_geral\
        FROM manutencaoVeiculo AS Mv\
            LEFT JOIN itemManutencao AS Im\
            ON Mv.id = Im.manutencaoVeiculo_id\
            LEFT JOIN veiculo AS Ve\
            ON Mv.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Mv.colaborador_id = Col.id\
            LEFT JOIN fornecedor AS Fo\
            ON Im.fornecedor_id = Fo.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        manutencao = decimal_to_float.default(dados)
        dicio = {"items": manutencao}
        result = self.cria_retorno_manutencao(dicio)
        return result

    def list_intervalo_manutencao(self, ano, mes):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Mv.*,Mv.id as id_manutencao, Im.*, Fo.nome as fornecedor, Ve.placa,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        monthname(Mv.data_inicial) as mes,\
        ifnull((select sum(preco) from itemManutencao where manutencaoVeiculo_id = Mv.id), 0) as total_itens,\
        ifnull((select sum(preco) from itemManutencao), 0) as total_geral\
        FROM manutencaoVeiculo AS Mv\
            LEFT JOIN itemManutencao AS Im\
            ON Mv.id = Im.manutencaoVeiculo_id\
            LEFT JOIN veiculo AS Ve\
            ON Mv.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Mv.colaborador_id = Col.id\
            LEFT JOIN fornecedor AS Fo\
            ON Im.fornecedor_id = Fo.id\
        WHERE YEAR(Mv.data_inicial) = %s AND MONTH(Mv.data_inicial) = %s"
        valor = (ano, mes)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        manutencao = decimal_to_float.default(dados)
        dicio = {"items": manutencao}
        result = self.cria_retorno_manutencao(dicio)
        return result

    def find_manutencao(self, id_manutencao):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Mv.*,Mv.id as id_manutencao, Im.*, Fo.nome as fornecedor, Ve.placa,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        monthname(Mv.data_inicial) as mes,\
        ifnull((select sum(preco) from itemManutencao where manutencaoVeiculo_id = Mv.id), 0) as total_itens\
        FROM manutencaoVeiculo AS Mv\
            LEFT JOIN itemManutencao AS Im\
            ON Mv.id = Im.manutencaoVeiculo_id\
            LEFT JOIN veiculo AS Ve\
            ON Mv.veiculo_id = Ve.id\
            LEFT JOIN colaborador AS Col\
            ON Mv.colaborador_id = Col.id\
            LEFT JOIN fornecedor AS Fo\
            ON Im.fornecedor_id = Fo.id\
        WHERE Mv.id=%s\
        order by mes"
        valor = (id_manutencao,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        manutencao = decimal_to_float.default(dados)
        dicio = {"items": manutencao}
        result = self.cria_retorno_manutencao(dicio)
        return result["items"][0]

    def save_manutencao(self, manutencao, listaItem):
        db = start_db()
        cursor = db.cursor()
        sqlQuery1 = "INSERT INTO manutencaoVeiculo(\
        id,\
        veiculo_id,\
        colaborador_id,\
        data_inicial,\
        data_final)\
        VALUES(%s, %s, %s, %s, %s)"
        dados1 = (
            manutencao._id, manutencao._veiculo_id, manutencao._colaborador_id,
            manutencao._data_inicial, manutencao._data_final
        )
        sqlQuery2 = "INSERT INTO itemManutencao(\
        id,\
        tipo,\
        nome,\
        preco,\
        fornecedor_id,\
        manutencaoVeiculo_id)\
        VALUES(%s, %s, %s, %s, %s, %s)"
        dados2 = []
        for dicio in listaItem:
            dados2.append((
                dicio._id, dicio._tipo, dicio._nome,
                dicio._preco, dicio._fornecedor_id,
                dicio._manutencaoVeiculo_id
            ))
        try:
            cursor.execute(sqlQuery1, dados1)
            cursor.executemany(sqlQuery2, dados2)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning, TypeError, ValueError) as e:
            self._errorMsg = str(e)
            cursor.close()
            return False

    def update_manutencao(self, manutencao, novosItens, atuaisItens):
        db = start_db()
        cursor = db.cursor()
        sqlQuery1 = "UPDATE manutencaoVeiculo SET\
        veiculo_id = %s,\
        colaborador_id = %s,\
        data_inicial = %s,\
        data_final = %s\
        WHERE id = %s"
        valor = manutencao._id
        dados1 = (
            manutencao._veiculo_id, manutencao._colaborador_id,
            manutencao._data_inicial, manutencao._data_final, valor
        )
        sqlQuery2 = "UPDATE itemManutencao SET\
        tipo = %s,\
        nome = %s,\
        preco = %s,\
        fornecedor_id = %s,\
        manutencaoVeiculo_id = %s\
        WHERE id  = %s"
        dados2 = []
        for dicio in atuaisItens:
            dados2.append((
                dicio._tipo, dicio._nome,
                dicio._preco, dicio._fornecedor_id,
                dicio._manutencaoVeiculo_id, dicio._id
            ))
        sqlQuery3 = "INSERT INTO itemManutencao(\
        id,\
        tipo,\
        nome,\
        preco,\
        fornecedor_id,\
        manutencaoVeiculo_id)\
        VALUES(%s, %s, %s, %s, %s, %s)"
        dados3 = []
        for dicio in novosItens:
            dados3.append((
                dicio._id, dicio._tipo, dicio._nome,
                dicio._preco, dicio._fornecedor_id,
                dicio._manutencaoVeiculo_id
            ))
        try:
            cursor.execute(sqlQuery1, dados1)
            cursor.executemany(sqlQuery2, dados2)
            cursor.executemany(sqlQuery3, dados3)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning, TypeError, ValueError) as e:
            self._errorMsg = str(e)
            cursor.close()
            return False

    def delete_manutencao(self, id_manutencao):
        db = start_db()
        cursor = db.cursor()
        sqlQuery1 = "DELETE FROM manutencaoVeiculo WHERE id = %s"
        sqlQuery2 = "DELETE FROM itemManutencao WHERE manutencaoVeiculo_id = %s"
        valor = (id_manutencao,)
        cursor.execute(sqlQuery2, valor)
        cursor.execute(sqlQuery1, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg

    def cria_retorno_manutencao(self, lista_manutencao):
        lista_dicio = []
        for dicio_manutencao in lista_manutencao["items"]:
            if lista_dicio == []:
                dicio_manutencao["item_manutencao"] = []
                if dicio_manutencao["id"] is not None:
                    dicio_manutencao["item_manutencao"].append({
                        "id": dicio_manutencao.pop("id"),
                        "tipo": dicio_manutencao.pop("tipo"),
                        "nome": dicio_manutencao.pop("nome"),
                        "preco": dicio_manutencao.pop("preco"),
                        "fornecedor_id": dicio_manutencao.pop("fornecedor_id"),
                        "manutencaoVeiculo_id": dicio_manutencao.pop("manutencaoVeiculo_id"),
                        "fornecedor": dicio_manutencao.pop("fornecedor")
                    })
                lista_dicio.append(dicio_manutencao)
            else:
                resp = [dicio for dicio in lista_dicio if dicio["id_manutencao"] == dicio_manutencao["id_manutencao"]]
                if resp != []:
                    if dicio_manutencao["id"] is not None:
                        resp[0]["item_manutencao"].append({
                            "id": dicio_manutencao.pop("id"),
                            "tipo": dicio_manutencao.pop("tipo"),
                            "nome": dicio_manutencao.pop("nome"),
                            "preco": dicio_manutencao.pop("preco"),
                            "fornecedor_id": dicio_manutencao.pop("fornecedor_id"),
                            "manutencaoVeiculo_id": dicio_manutencao.pop("manutencaoVeiculo_id"),
                            "fornecedor": dicio_manutencao.pop("fornecedor")
                        })
                else:
                    dicio_manutencao["item_manutencao"] = []
                    if dicio_manutencao["id"] is not None:
                        dicio_manutencao["item_manutencao"].append({
                            "id": dicio_manutencao.pop("id"),
                            "tipo": dicio_manutencao.pop("tipo"),
                            "nome": dicio_manutencao.pop("nome"),
                            "preco": dicio_manutencao.pop("preco"),
                            "fornecedor_id": dicio_manutencao.pop("fornecedor_id"),
                            "manutencaoVeiculo_id": dicio_manutencao.pop("manutencaoVeiculo_id"),
                            "fornecedor": dicio_manutencao.pop("fornecedor")
                        })
                    lista_dicio.append(dicio_manutencao)
        dicio = {"items": lista_dicio}
        return dicio


class DecimalEncoder:
    def default(self, list_dicio):
        for dicio in list_dicio:
            for key, valor in dicio.items():
                if isinstance(valor, D):
                    dicio[key] = float(valor)
        return list_dicio
