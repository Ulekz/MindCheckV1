import sqlite3
from werkzeug.security import generate_password_hash

def crear_bd():
    conn = sqlite3.connect('mindcheck.db')
    cursor = conn.cursor()

    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL
        )
    ''')

    # Crear tabla de mensajes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            texto TEXT,
            fecha TEXT
        )
    ''')

    # Insertar un usuario admin si no existe
    cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', ('admin',))
    if not cursor.fetchone():
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (
            'admin',
            generate_password_hash('admin123')  # Cambia esta contraseña en producción
        ))
        print("Usuario admin creado")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    crear_bd()
