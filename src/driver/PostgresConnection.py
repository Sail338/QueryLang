import psycopg2

from driver.Connection import Connection


class PostgresConnection(Connection):
    def __init__(self, username: str, db_name: str, password, port: int=5432, host: str="localhost"):
        self.host = host
        self.db_name = db_name
        self.username = username
        self.port = port
        self.password = password


    def connect(self):
         con = psycopg2.connect(f"dbname={db_name} user={self.username} password={self.password} host={self.host} port={self.port}")
         return con
