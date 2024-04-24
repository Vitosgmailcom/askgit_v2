from src.DAO.connectDB import ConnectDB

import random

class HelperDB(object):
    def __init__(self):
        self.conn = ConnectDB()

    def get_random_user(self, sql, qty=None):
        if not qty:
            qty = 5
        result = self.conn.execute_SELECT(sql)
        return random.sample(result, qty)

