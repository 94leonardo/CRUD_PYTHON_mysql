import mysql.connector
from Conexion import *


class CClientes:

    # Modificar Clientes
    @staticmethod
    def mostrarClientes():

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar a la base de datos {}", format(error))

# Ingresar Clientes
    @staticmethod
    def ingresarClientes(nombres, apellidos, sexo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()

            sql = "insert into usuarios values(null,%s,%s,%s);"
            # la variable valores tiene que ser una tubla
            # como minima exprecion es: (valor,) la coma hace que sea una TUPLA las tuplas son lista inmutables no se puede modificar

            valores = (nombres, apellidos, sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

# Modificar clientes
    @staticmethod
    def modificarClientes(idUsuarios, nombres, apellidos, sexo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()

            sql = "update usuarios set  usuarios.nombres = %s,usuarios.apellidos =%s,usuarios.sexo=%s where usuarios.id =%s;"
            valores = (nombres, apellidos, sexo, idUsuarios)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al Actualizado a la base de datos {}", format(error))

# Eliminar clientes
    @staticmethod
    def EliminarClientes(idUsuarios):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()

            sql = "delete from usuarios where usuarios.id=%s;"
            valores = (idUsuarios,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al Eliminar a la base de datos {}", format(error))
