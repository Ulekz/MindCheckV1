import sqlite3

def migrar_db():
    conn = sqlite3.connect('mindcheck.db')
    cursor = conn.cursor()

    # Agregar campo 'telefono' si no existe
    try:
        cursor.execute("ALTER TABLE mensajes ADD COLUMN telefono TEXT")
    except sqlite3.OperationalError:
        print("Columna 'telefono' ya existe.")

    # Agregar campo 'es_emergencia' si no existe
    try:
        cursor.execute("ALTER TABLE mensajes ADD COLUMN es_emergencia INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        print("Columna 'es_emergencia' ya existe.")

    conn.commit()
    conn.close()
    print("Migración completada.")

if __name__ == '__main__':
    migrar_db()
