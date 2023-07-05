import mariadb
from DB.conexion import conectar
from clase.usuario import Persona

class AccesoDB():

    def insert(nombre, edad,telefono,email):
        try:
            conn = conectar()
            conn.cursor().execute(
                'INSERT INTO personaTabla (nombre,edad,telefono,email) VALUES(%s,%s,%s,%s)',
                (nombre,edad,telefono,email)
            )
            conn.commit()
            conn.close()
            return "exito"
        except mariadb.Error as e:
            print(f"{e}")
            return "error"
        
    def select():
        lista = []
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute(
                'SELECT id,nombre,edad,telefono,email FROM personaTabla'
            )
            for id,nombre,edad,telefono,email in cur: 
                persona = Persona(id,nombre,edad,telefono,email)
                lista.append(persona)
            conn.close()
        except mariadb.Error as e:
            print(f"Error de coneccion {e}")
        return lista 
        
    def delete(id):
        try:
            conn = conectar()
            conn.cursor().execute(
                'DELETE FROM personaTabla WHERE id = %s',
                (id)
            )
            conn.commit()
            conn.close()
            return "exito"
        except mariadb.Error as e:
            print(f"{e}")
            return "error"

    def update(id,nombre,edad,telefono,email):
        try:
            conn = conectar()
            conn.cursor().execute(
                'UPDATE personaTabla SET nombre = %s,edad = %s,telefono = %s,email = %s WHERE id=%s',
                (nombre,edad,telefono,email,id)
            )
            conn.commit()
            conn.close()
            return "exito"
        except mariadb.Error as e:
            print(f"{e}")
            return "error"
    
    def consulta(ide):
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute(
                'SELECT id,nombre,edad,telefono,email FROM personaTabla'
            )
            for id,nombre,edad,telefono,email in cur: 
                if id == ide:
                    persona = Persona(id,nombre,edad,telefono,email)
            conn.close()
            return persona
        except mariadb.Error as e:
            return f"Error de coneccion {e}"
        