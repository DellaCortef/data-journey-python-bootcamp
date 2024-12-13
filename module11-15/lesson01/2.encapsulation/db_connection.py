from sqlite import SQLiteDatabase
from postgres import DatabasePost
from encaps import DataBase

def execute_on_database(database, query):
    database.connect()
    database.execute_query(query)
    database.disconnect()

# SQLite Example
sql_bank = SQLiteDatabase("example.db")
sqlite_query = """
INSERT INTO users (name, email) VALUES
('John', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
execute_on_database(sql_bank, sqlite_query)

# PostgreSQL Example
postgres_bank = DatabasePost('localhost', '5432', 'bank_name', 'user', 'password')
postgres_query = """
INSERT INTO users (name, email) VALUES
('John', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
execute_on_database(postgres_bank, postgres_query)
