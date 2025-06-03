import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('mindcheck.db')
cursor = conn.cursor()

# Intenta agregar la columna solo si no existe
try:
    cursor.execute("ALTER TABLE usuarios_registrados ADD COLUMN contraseña_hash TEXT")
    print("✅ Columna 'contraseña_hash' agregada correctamente.")
except sqlite3.OperationalError as e:
    print("⚠️ No se pudo agregar la columna (puede que ya exista):", e)

conn.commit()
conn.close()
