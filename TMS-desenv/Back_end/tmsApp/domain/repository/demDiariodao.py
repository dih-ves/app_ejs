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


class DemDiarioDAO:
    def __init__(self):
        self._errorMsg = None

    def list_demonstrativo_diario(self):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Dd.*, Dd.hodometro_fim-Dd.hodometro_ini as km_rodado_dia,\
        day(data) as dia, monthname(data) as mes, YEAR(data) as ano,\
        timediff(Dd.horario_fim, Dd.horario_ini) as horas_trabalhadas,\
        round(TIMESTAMPDIFF(minute, Dd.horario_ini, Dd.horario_fim)*(ifnull(valor_hora,0)/60), 2) as total_dia,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        day(data) as dia, monthname(data) as mes, year(data) as ano,\
        Ve.placa as 'veiculo utilizado',\
        (SELECT ifnull(cast(sum(hodometro_fim-hodometro_ini) as SIGNED),0) FROM ddsp) as total_km_mes,\
        (SELECT ifnull(cast(sum(timediff(horario_fim, horario_ini)) as TIME),0) FROM ddsp) as total_horas_mes,\
        (SELECT ifnull(sum(round(TIMESTAMPDIFF(minute, horario_ini, horario_fim)*(ifnull(valor_hora,0)/60), 2)),0) FROM ddsp) as vencimentos_totais\
        FROM ddsp AS Dd\
            LEFT JOIN colaborador AS Col\
            ON Dd.colaborador_id = Col.id\
            LEFT JOIN veiculo AS Ve\
            ON Dd.veiculo_id = Ve.id"
        cursor.execute(sqlQuery)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        demDiario = decimal_to_float.default(dados)
        for dicio in demDiario:
            if "horario_ini" in dicio:
                dicio["horario_ini"] = str(dicio["horario_ini"])
            if "horario_fim" in dicio:
                dicio["horario_fim"] = str(dicio["horario_fim"])
            if "horas_trabalhadas" in dicio:
                dicio["horas_trabalhadas"] = str(dicio["horas_trabalhadas"])
        dicio = {"items": demDiario}
        return dicio

    def list_intervalo_demonstrativo_diario(self, ano, mes):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Dd.*, Dd.hodometro_fim-Dd.hodometro_ini as km_rodado_dia,\
        day(data) as dia, monthname(data) as mes, YEAR(data) as ano,\
        timediff(Dd.horario_fim, Dd.horario_ini) as horas_trabalhadas,\
        round(TIMESTAMPDIFF(minute, Dd.horario_ini, Dd.horario_fim)*(ifnull(valor_hora,0)/60), 2) as total_dia,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        day(data) as dia, monthname(data) as mes, year(data) as ano,\
        Ve.placa as 'veiculo utilizado',\
        (SELECT ifnull(cast(sum(hodometro_fim-hodometro_ini) as SIGNED),0) FROM ddsp WHERE year(data) = %s and month(data) = %s) as total_km_mes,\
        (SELECT ifnull(cast(sum(timediff(horario_fim, horario_ini)) as TIME),0) FROM ddsp WHERE year(data) = %s and month(data) = %s) as total_horas_mes,\
        (SELECT ifnull(sum(round(TIMESTAMPDIFF(minute, horario_ini, horario_fim)*(ifnull(valor_hora,0)/60), 2)),0) FROM ddsp WHERE year(data) = %s and month(data) = %s) as vencimentos_totais\
        FROM ddsp AS Dd\
            LEFT JOIN colaborador AS Col\
            ON Dd.colaborador_id = Col.id\
            LEFT JOIN veiculo AS Ve\
            ON Dd.veiculo_id = Ve.id\
        WHERE year(data) = %s and month(data) = %s"
        valor = (ano, mes, ano, mes, ano, mes, ano, mes)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return None
        decimal_to_float = DecimalEncoder()
        demDiario = decimal_to_float.default(dados)
        for dicio in demDiario:
            if "horario_ini" in dicio:
                dicio["horario_ini"] = str(dicio["horario_ini"])
            if "horario_fim" in dicio:
                dicio["horario_fim"] = str(dicio["horario_fim"])
            if "horas_trabalhadas" in dicio:
                dicio["horas_trabalhadas"] = str(dicio["horas_trabalhadas"])
            if "total_horas_mes" in dicio:
                dicio["total_horas_mes"] = str(dicio["total_horas_mes"])
        dicio = {"items": demDiario}
        return dicio

    def find_demonstrativo_diario(self, id_demDiario):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT\
        Dd.*, Dd.hodometro_fim-Dd.hodometro_ini as km_rodado_dia,\
        day(data) as dia, monthname(data) as mes, YEAR(data) as ano,\
        timediff(Dd.horario_fim, Dd.horario_ini) as horas_trabalhadas,\
        round(TIMESTAMPDIFF(minute, Dd.horario_ini, Dd.horario_fim)*(ifnull(valor_hora,0)/60),2) as total_dia,\
        concat(Col.nome,' ', Col.sobrenome) as colaborador,\
        day(data) as dia, monthname(data) as mes, year(data) as ano,\
        Ve.placa as 'veiculo utilizado'\
        FROM ddsp AS Dd\
            LEFT JOIN colaborador AS Col\
            ON Dd.colaborador_id = Col.id\
            LEFT JOIN veiculo AS Ve\
            ON Dd.veiculo_id = Ve.id\
        WHERE Dd.id = %s "
        valor = (id_demDiario,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        decimal_to_float = DecimalEncoder()
        demDiario = decimal_to_float.default(dados)
        if demDiario is None or demDiario == []:
            return None
        if len(demDiario) > 0:
            demDiario[0]["horario_ini"] = str(demDiario[0]["horario_ini"])
            demDiario[0]["horario_fim"] = str(demDiario[0]["horario_fim"])
            demDiario[0]["horas_trabalhadas"] = str(demDiario[0]["horas_trabalhadas"])
        return demDiario[0]

    def save_demonstrativo_diario(self, demDiario):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO ddsp (\
        id,\
        data,\
        hodometro_ini,\
        hodometro_fim,\
        horario_ini,\
        horario_fim,\
        intervalo_ini,\
        intervalo_fim,\
        usuario_sr,\
        valor_hora,\
        colaborador_id,\
        veiculo_id)\
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (
            demDiario._id,
            demDiario._data,
            demDiario._hodometro_ini,
            demDiario._hodometro_fim,
            demDiario._horario_ini,
            demDiario._horario_fim,
            demDiario._intervalo_ini,
            demDiario._intervalo_fim,
            demDiario._usuario_sr,
            demDiario._valor_hora,
            demDiario._colaborador_id,
            demDiario._veiculo_id
        )
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def update_demonstrativo_diario(self, demDiario):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "UPDATE ddsp SET\
        data = %s,\
        hodometro_ini = %s,\
        hodometro_fim = %s,\
        horario_ini = %s,\
        horario_fim = %s,\
        intervalo_ini = %s,\
        intervalo_fim = %s,\
        usuario_sr = %s,\
        valor_hora = %s,\
        colaborador_id = %s,\
        veiculo_id = %s\
        WHERE id = %s"
        valor = demDiario._id
        dados = (
            demDiario._data,
            demDiario._hodometro_ini,
            demDiario._hodometro_fim,
            demDiario._horario_ini,
            demDiario._horario_fim,
            demDiario._intervalo_ini,
            demDiario._intervalo_fim,
            demDiario._usuario_sr,
            demDiario._valor_hora,
            demDiario._colaborador_id,
            demDiario._veiculo_id,
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

    def delete_demonstrativo_diario(self, id_demDiario):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "DELETE FROM ddsp WHERE id = %s"
        valor = (id_demDiario,)
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
