import mariadb

def conectar():
    conn = mariadb.connect(
        host = "localhost",
        database = "personadb",
        user="admin",
        password = "fallout",
        port = 3306
        )
    return conn

    
