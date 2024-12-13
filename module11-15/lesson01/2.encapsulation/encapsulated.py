import os
import them
import sqlite3
import psycopg2

class DataBase:
    def __init__(self, bank_type):
        self.bank_type = bank_type
        self.connection = None

    def connect(self):
        if self.bank_type == 'sqlite':
            try:
                file_name = os.getenv('SQLITE_FILENAME')
                self.connection = sqlite3.connect(file_name)
                print("SQLite connection established successfully!")
            except sqlite3.Error as e:
                print("Error connecting to SQLite database:", e)
        elif self.bank_type == 'postgres':
            try:
                host = os.getenv('HOST_PG')
                port = os.getenv('PORTA_PG')
                bank = os.getenv('BANK_PG')
                user = os.getenv('USER_PG')
                password = os.getenv('PASSWORD_PG')
                self.connection = psycopg2.connect(
                    host=host,
                    port=port,
                    database=bank,
                    user=user,
                    password=password
                )
                print("PostgreSQL connection established successfully!")
            except psycopg2.Error as e:
                print("Error connecting to PostgreSQL database:", e)
        else:
            print("Database type not supported.")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            if self.bank_type == 'sqlite':
                print("SQLite connection closed.")
            elif self.bank_type == 'postgres':
                print("PostgreSQL connection closed.")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully!")
        except (sqlite3.Error, psycopg2.Error) as e:
            print("Error executing query:", e)


# Usage example
if __name__ == "__main__":
    type_bank = os.getenv('bank_type') # 'sqlite' or 'postgres'
    
    bank = DataBase(sqlite3)
    bank.connect()

    # Example of table creation
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    bank.execute_query(create_table_query)

    # Data insertion example
    insert_query = """
    INSERT INTO users (name, email) VALUES
    ('John', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """
    bank.execute_query(insert_query)

    bank.disconnect()