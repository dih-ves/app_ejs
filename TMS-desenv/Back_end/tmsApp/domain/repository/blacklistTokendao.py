import mysql.connector as mysql


def start_db():
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="tiagodatabase84",
        database="tms",
    )
    return db


class BlacklistTokenDAO():
    def check_blacklistToken(self, auth_token):
        db = start_db()
        cursor = db.cursor(dictionary=True)
        sqlQuery = "SELECT token FROM blacklistToken WHERE token = %s"
        valor = (auth_token,)
        cursor.execute(sqlQuery, valor)
        dados = cursor.fetchall()
        if dados is None or dados == []:
            return False
        return True

    def save_token(self, blacklistToken):
        db = start_db()
        cursor = db.cursor()
        sqlQuery = "INSERT INTO blacklistToken(token, blacklisted_em)\
        values(%s, %s)"
        dados = (blacklistToken._token, blacklistToken._blacklisted_em)
        try:
            cursor.execute(sqlQuery, dados)
            db.commit()
            cursor.close()
            return True
        except (mysql.Error, mysql.Warning) as e:
            self._errorMsg = str(e)
            return False

    def get_error(self):
        return self._errorMsg
