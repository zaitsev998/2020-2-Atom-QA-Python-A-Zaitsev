import pymysql
from pymysql.cursors import DictCursor


class MysqlConnection(object):

    def __init__(self, user, password, db_name, host, port, charset='utf8'):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port
        self.charset = charset
        self.connection = self.connect()

    def get_connection(self, db_created=False):
        return pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               db=self.db_name if db_created else None,
                               charset=self.charset, cursorclass=DictCursor, autocommit=True)

    def connect(self):
        connection = self.get_connection()

        connection.query(f'DROP DATABASE IF EXISTS {self.db_name}')
        connection.query(f'CREATE DATABASE {self.db_name}')
        connection.close()

        return self.get_connection(db_created=True)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
