import mysql.connector as mysql
from decimal import Decimal as D


# cria a conexao com o banco
def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class VeiculoDAO:
    def __init__(self):
        self._errorMsg = None

    def list_veiculo(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        ve.*,\
        ifnull((Ve.valor_ipva+Ve.valor_licenciamento+Ve.valor_dpvat), 0) AS total_taxas,\
        Mu.codigo_ait as multa, Mu.valor as valor_multa,\
        ifnull((select sum(valor) from multa where veiculo_id = Ve.id),0) as total_multas,\
        ifnull((Ve.valor_ipva+Ve.valor_licenciamento+Ve.valor_dpvat), 0)+\
        ifnull((select sum(valor) from multa where veiculo_id = Ve.id),0) as total,\
        ifnull((select sum(valor_ipva) from veiculo),0) as total_ipva,\
        ifnull((select sum(valor_licenciamento) from veiculo),0) as total_licenciamento,\
        ifnull((select sum(valor_dpvat) from veiculo),0) as total_dpvat,\
        ifnull((select sum(valor) from multa),0) as total_de_multas,\
        ((select sum(valor_ipva) from veiculo)+\
        (select sum(valor_licenciamento) from veiculo)+\
        (select sum(valor_dpvat) from veiculo)+\
        (select sum(valor) from multa)) as total_tabela\
        FROM veiculo AS Ve\
        left JOIN multa as Mu\
        ON Ve.id = Mu.veiculo_id\
        ORDER BY Ve.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        veiculo = decimal_to_float.default(dados)
        dicio = {"items": veiculo}
        result = self.cria_retorno_veiculo(dicio)
        return result

    def find_veiculo(self, id_veiculo):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        ve.*,\
        ifnull((Ve.valor_ipva+Ve.valor_licenciamento+Ve.valor_dpvat), 0) AS total_taxas,\
        Mu.codigo_ait as multa, Mu.valor as valor_multa,\
        ifnull((select sum(valor) from multa where veiculo_id = Ve.id),0) as total_multas,\
        ifnull((Ve.valor_ipva+Ve.valor_licenciamento+Ve.valor_dpvat), 0)+\
        ifnull((select sum(valor) from multa where veiculo_id = Ve.id),0) as total\
        FROM veiculo AS Ve\
        left JOIN multa as Mu\
        ON Ve.id = Mu.veiculo_id\
        WHERE Ve.id = %s "
        valor = (id_veiculo,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        veiculo = decimal_to_float.default(dados)
        dicio = {"items": veiculo}
        result = self.cria_retorno_veiculo(dicio)
        return result["items"][0]

    def save_veiculo(self, veiculo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO veiculo (\
        id,\
        marca,\
        placa,\
        ano,\
        renavam,\
        mes_licenciamento,\
        vencimento_ipva,\
        status,\
        valor_ipva,\
        valor_licenciamento,\
        valor_dpvat)\
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,\
        %s, %s, %s)"
        dados = (
            veiculo._id, veiculo._marca, veiculo._placa,
            veiculo._ano, veiculo._renavam, veiculo._mes_licenciamento,
            veiculo._vencimento_ipva, veiculo._status, veiculo._valor_ipva,
            veiculo._valor_licenciamento, veiculo._valor_dpvat
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_veiculo(self, veiculo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE veiculo SET\
        marca = %s,\
        placa = %s,\
        ano = %s,\
        renavam = %s,\
        mes_licenciamento = %s,\
        vencimento_ipva = %s,\
        status = %s,\
        valor_ipva = %s,\
        valor_licenciamento = %s,\
        valor_dpvat = %s\
        WHERE id = %s"
        valor = veiculo._id
        dados = (
            veiculo._marca, veiculo._placa,
            veiculo._ano, veiculo._renavam, veiculo._mes_licenciamento,
            veiculo._vencimento_ipva, veiculo._status, veiculo._valor_ipva,
            veiculo._valor_licenciamento, veiculo._valor_dpvat, valor
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def delete_veiculo(self, id_veiculo):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM veiculo WHERE id = %s"
        valor = (id_veiculo,)
        cursor.execute(sqlQuery, valor)
        db.commit()
        cursor.close()

    def get_error(self):
        return self._errorMsg

    # metodo para unir veiculos duplicados e
    # gerar lista de multas para o veiculo
    def cria_retorno_veiculo(self, lista_veiculos):
        lista_dicio = []
        for dicio_veiculo in lista_veiculos["items"]:
            if lista_dicio == []:
                dicio_veiculo["lista_multas"] = []
                if dicio_veiculo["multa"] is not None:
                    dicio_veiculo["lista_multas"].append({"multa": dicio_veiculo.pop("multa"), "valor_multa": dicio_veiculo.pop("valor_multa")})
                lista_dicio.append(dicio_veiculo)
            else:
                resp = [dicio for dicio in lista_dicio if dicio["id"] == dicio_veiculo["id"]]
                if resp != []:
                    if dicio_veiculo["multa"] is not None:
                        resp[0]["lista_multas"].append({"multa": dicio_veiculo.pop("multa"), "valor_multa": dicio_veiculo.pop("valor_multa")})
                else:
                    dicio_veiculo["lista_multas"] = []
                    if dicio_veiculo["multa"] is not None:
                        dicio_veiculo["lista_multas"].append({"multa": dicio_veiculo.pop("multa"), "valor_multa": dicio_veiculo.pop("valor_multa")})
                    lista_dicio.append(dicio_veiculo)
        dicio = {"items": lista_dicio}
        return dicio


class DecimalEncoder:
    def default(self, list_dicio):
        for dicio in list_dicio:
            for key, valor in dicio.items():
                if isinstance(valor, D):
                    dicio[key] = float(valor)
            print(list_dicio)
        return list_dicio
