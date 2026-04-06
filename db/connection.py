import psycopg2

DB_CONFIG = {
    "host": "192.168.0.104",
    "port": 5430,
    "dbname": "auth",
    "user": "postgres",
    "password": 1234

}

class DBConnection:
    def __init__(self):
        self.conn  = psycopg2.connect(**DB_CONFIG)

    def execute(self, query, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

db = DBConnection()

result = db.execute("SELECT * from public.users;")
print(result)