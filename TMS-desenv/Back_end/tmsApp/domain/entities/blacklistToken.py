import datetime


class BlacklistToken:
    def __init__(self, token):
        self._token = token
        self._blacklisted_em = datetime.datetime.utcnow()
