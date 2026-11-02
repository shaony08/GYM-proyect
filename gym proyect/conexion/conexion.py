import os
import sqlite3

# Constante global con la ruta física hacia el archivo de base de datos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_BD = os.path.join(BASE_DIR, "base de datos", "gym_data_base.db")


#def conectar():
    #   '''Establece y retorna un nuevo objeto de conexión con la base de datos SQLite.'''
    #  return sqlite3.connect(RUTA_BD)
def conectar():

    print("BASE DE DATOS:", RUTA_BD)

    return sqlite3.connect(RUTA_BD)

##obteber todas las clientes
def clientes():
    '''Operación READ: Recupera los clientes ID.'''
    conexion = conectar()
    try:
        cursor = conexion.cursor()
    # Proyección explícita de las 7 columnas para garantizar correspondencia con la GUI
        cursor.execute(
            "SELECT  id_cliente, nombre, apellido, telefono, fecha_inicio, fecha_vencimiento"
            " FROM clientes ORDER BY id_cliente ASC"
            )
    # fetchall() extrae todas las filas y las retorna como una lista de tuplas
        return cursor.fetchall()
    finally:
    # El bloque finally garantiza el cierre inmediato de la conexión para evitar bloqueos
        conexion.close()
        
##insertar nuevos clientes
def insertar_cliente(nombre, apellido, telefono, fecha_inicio, fecha_vencimiento, id_suscripcion):
    '''Operación CREATE: Inserta un nuevo registro utilizando tuplas parametrizadas.'''
    conexion = conectar()
    try:
        cursor = conexion.cursor()
    # El uso de signos de interrogación (?) previene ataques de inyección SQL
        sql_insert = (
            "INSERT INTO clientes "
            "(nombre, apellido, telefono, fecha_inicio, fecha_vencimiento, id_suscripcion) "
            "VALUES (?, ?, ?, ?, ?, ?)"
            )
        valores = (nombre, apellido, telefono, fecha_inicio, fecha_vencimiento, id_suscripcion)
        cursor.execute(sql_insert, valores)
    # commit() confirma y asienta físicamente la transacción en el archivo .db
        conexion.commit()
    finally:
        conexion.close()

#actualizar suscripciones
def buscar_cliente(nombre):
    '''Operación READ: Recupera los datos de un cliente por su nombre.'''
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_cliente, nombre, apellido FROM clientes WHERE nombre = ?", (nombre,))
        return cursor.fetchone()
    finally:
        conexion.close()
        
#actualizar suscripciones
def buscar_entrenador(nombre):
    '''Operación READ: Recupera los datos de un entrenador por su nombre.'''
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_entrenador, nombre, horario FROM entrenadores WHERE nombre = ?", (nombre,))
        return cursor.fetchone()
    finally:
        conexion.close()
        

#obtener entrenadores
def obtener_entrenadores():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_entrenador,
                    nombre,
                    horario,
                    contacto,
                    pago
            FROM entrenadores
            ORDER BY id_entrenador
        """)
        return cursor.fetchall()
    finally:
        conexion.close()

def obtener_asistencias():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_asistencias,
                    fechas,
                    hora_entrada,
                    id_cientes,
                    nombre
            FROM asistencias
            ORDER BY id_asistencias
        """)
        return cursor.fetchall()
    finally:
        conexion.close()
"""Necesito revisar y hacer cambios"""
##obtener maquinas libres
def obtener_maquinas_libres():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT m.id_maquinas,
                    m.nombre,
                    e.nombre AS estado
            FROM maquinas m
            LEFT JOIN estado e ON e.id_estado = m.estados
            WHERE LOWER(COALESCE(e.nombre, '')) IN ('Disponible', 'Reparada')
            ORDER BY m.id_maquinas
        """)
        return cursor.fetchall()
    finally:
        conexion.close()

#obtener maquinas ocupadas
def obtener_maquinas_ocupadas():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT m.id_maquinas,
                    m.nombre,
                    e.nombre AS estado
            FROM maquinas m
            LEFT JOIN estado e ON e.id_estado = m.estados
            WHERE LOWER(COALESCE(e.nombre, '')) IN ('Mantenimiento', 'En revisión')
            ORDER BY m.id_maquinas
        """)
        return cursor.fetchall()
    finally:
        conexion.close()

def obtener_maquinas_fuera_servicio():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT m.id_maquinas,
                    m.nombre,
                    e.nombre AS estado
            FROM maquinas m
            LEFT JOIN estado e ON e.id_estado = m.estados
            WHERE LOWER(COALESCE(e.nombre, '')) = 'fuera de servicio'
            ORDER BY m.id_maquinas
        """)
        return cursor.fetchall()
    finally:
        conexion.close()

def registro_de_pagos():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM registrar_pago
        """)
        print("TOTAL:", cursor.fetchone())
        cursor.execute("""
            SELECT *
            FROM registrar_pago
        """)
        datos = cursor.fetchall()
        print("REGISTROS:", datos)
        return datos
    finally:
        conexion.close()
        
def buscar_asistencias(nombre):
    '''Operación READ: Recupera los datos de un entrenador por su nombre.'''
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_asistencias, fechas, hora_entrada, id_clientes, nombre FROM asistencias WHERE nombre = ?", (nombre,))
        return cursor.fetchone()
    finally:
        conexion.close()
        