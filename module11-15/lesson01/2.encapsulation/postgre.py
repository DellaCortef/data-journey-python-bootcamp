import psycopg2

class DatabasePost:
    def __init__(self, host, port, bank, user, password):
        self.host = host
        self.port = port
        self.bank = bank
        self.user = user
        self.password = password
        self.conexao = None

    def connect(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.bank,
                user=self.user,
                password=self.password
            )
            print("Connection established successfully!")
        except psycopg2.Error as e:
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
        except psycopg2.Error as e:
            print("Error executing query:", e)


# Usage example
if __name__ == "__main__":
    host = 'localhost'
    port = '5432'
    bank = 'bank_name'
    user = 'user'
    password = 'password'
    
    bank = DatabasePost(host, port, bank, user, password)
    bank.connect()

    # Example of table creation
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    bank.executar_query(create_table_query)

    # Data insertion example
    insert_query = """
    INSERT INTO users (name, email) VALUES
    ('John', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """
    bank.executar_query(insert_query)

    bank.disconnect()