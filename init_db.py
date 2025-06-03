import sqlite3
from werkzeug.security import generate_password_hash

def inicializar_bd():
    conn = sqlite3.connect('mindcheck.db')
    cursor = conn.cursor()

    # Crear tabla de usuarios normales
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios_registrados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            contraseña_hash TEXT NOT NULL
        )
    ''')

    # Crear tabla de administradores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')

    # Insertar un administrador por defecto si no existe
    cursor.execute('SELECT id FROM usuarios WHERE usuario = ?', ('admin',))
    if not cursor.fetchone():
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (
            'admin',
            generate_password_hash('admin123')  # ⚠️ Cambiar en producción
        ))
        print("✅ Administrador creado: admin")

    # Crear tabla de mensajes del formulario de contacto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            telefono TEXT,
            texto TEXT,
            fecha TEXT,
            es_emergencia INTEGER DEFAULT 0
        )
    ''')

    # Crear tabla para guardar los resultados de los test
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados_test (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            correo_usuario TEXT,
            puntaje INTEGER NOT NULL,
            nivel TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Base de datos creada y lista para usarse.")

if __name__ == '__main__':
    inicializar_bd()
