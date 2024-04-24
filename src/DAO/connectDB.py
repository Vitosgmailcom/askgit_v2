from src.Utility.credentials import credentials_DB
import pymysql.cursors

class ConnectDB:
    def __init__(self):
        self.cred = credentials_DB()


    def connect(self):
        connection = pymysql.connect(
            user=self.cred['DB_USER'],
            password=self.cred['DB_PASS'],
            database=self.cred['DB_NAME'],
            port=int(self.cred['DB_PORT']),
            host=self.cred['DB_HOST']
        )
        return connection


    def execute_SELECT(self, sql):
        connection = self.connect()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result



