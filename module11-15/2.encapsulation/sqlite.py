import sqlite3

class SQLiteDatabase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.conexao = None

    def connect(self):
        try:
            self.conexao = sqlite3.connect(self.file_name)
            print("Connection established successfully!")
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    def disconnect(self):
        if self.conexao:
            self.conexao.close()
            print("Connection closed.")

    def execute_query(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print("Query executed successfully!")
        except sqlite3.Error as e:
            print("Error executing query:", e)

# Usage example
if __name__ == "__main__":
    file_name = "example.db"
    database = SQLiteDatabase(file_name)
    bank.connect()

    # Creating a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    bank.executar_query(create_table_query)

    # Inserting data into the table
    insert_query = """
    INSERT INTO users (name, email) VALUES
    ('John', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """
    bank.executar_query(insert_query)

    bank.disconnect()