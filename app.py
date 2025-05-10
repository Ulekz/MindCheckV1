from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
from datetime import datetime
import sqlite3
from werkzeug.security import check_password_hash
import csv
from flask import make_response

app = Flask(__name__)
app.secret_key = 'clave-super-secreta'

@app.route('/')
def index():
    frases = [
        {"texto": "No tienes que tenerlo todo resuelto hoy. Respira, estás haciendo lo mejor que puedes.", "autor": "Desconocido"},
        {"texto": "Cuidar tu salud mental también es productividad.", "autor": "MindCheck"},
        {"texto": "Buscar ayuda no es un signo de debilidad, sino de valentía.", "autor": "Desconocido"},
        {"texto": "Tu bienestar importa. Un paso a la vez.", "autor": "MindCheck"},
        {"texto": "Está bien no estar bien todo el tiempo.", "autor": "Anónimo"},
        {"texto": "Hablar es parte de sanar.", "autor": "MindCheck"}
    ]
    frases_aleatorias = random.sample(frases, k=4)
    return render_template("index.html", frases=frases_aleatorias, now=datetime.now)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    puntaje_total = 0
    for i in range(1, 8):
        respuesta = request.form.get(f'pregunta{i}')
        if respuesta is not None:
            puntaje_total += int(respuesta)

    # Determinar nivel de ansiedad y recursos
    if puntaje_total <= 4:
        nivel = "Ansiedad mínima"
        mensaje = "Tu nivel de ansiedad es bajo. Continúa cuidando tu bienestar con hábitos saludables."
        recursos = [
            {
                "titulo": "Ejercicio de gratitud diario",
                "descripcion": "Escribe 3 cosas por las que estés agradecido cada día.",
                "enlace": "https://www.nimh.nih.gov/get-involved/digital-shareables/espanol/recursos-para-compartir-sobre-la-salud-mental-en-espanol",
                "boton": "Ver recursos"
            }
        ]
    elif puntaje_total <= 9:
        nivel = "Ansiedad leve"
        mensaje = "Es posible que experimentes síntomas leves. Intenta técnicas de relajación y hábitos de autocuidado."
        recursos = [
            {
                "titulo": "Técnicas de relajación para aliviar el estrés",
                "descripcion": "Métodos simples y gratuitos para reducir la ansiedad.",
                "enlace": "https://www.helpguide.org/es/ansiedad/tecnicas-de-relajacion-para-aliviar-el-estres",
                "boton": "Ver técnicas"
            },
            {
                "titulo": "Meditación guiada en español (5 min)",
                "descripcion": "Relajación guiada para calmar tu mente.",
                "enlace": "https://www.youtube.com/watch?v=3opO2_k2uhI",
                "boton": "Ver video"
            }
        ]
    elif puntaje_total <= 14:
        nivel = "Ansiedad moderada"
        mensaje = "Tus síntomas pueden interferir con tu vida diaria. Es buena idea buscar ayuda o guía emocional."
        recursos = [
            {
                "titulo": "Línea de la Vida – Apoyo psicológico gratuito",
                "descripcion": "Llama al 800 911 2000 para orientación profesional.",
                "enlace": "https://www.gob.mx/salud/articulos/linea-de-la-vida-ayuda-profesional-para-personas-con-depresion",
                "boton": "Más información"
            },
            {
                "titulo": "Consejo Ciudadano CDMX",
                "descripcion": "Atención emocional gratuita: 55 5533 5533.",
                "enlace": "https://consejociudadanomx.org/asi-te-ayudamos/contencion-emocional",
                "boton": "Visitar sitio"
            }
        ]
    else:
        nivel = "Ansiedad severa"
        mensaje = "Tus respuestas indican ansiedad severa. Es recomendable buscar apoyo psicológico cuanto antes. No estás solo/a."
        recursos = [
            {
                "titulo": "Directorio nacional de unidades de salud mental",
                "descripcion": "Encuentra ayuda cercana en todo México.",
                "enlace": "https://www.gob.mx/salud/acciones-y-programas/directorio-de-unidades-de-salud-mental",
                "boton": "Buscar ayuda"
            },
            {
                "titulo": "Atención psicológica CIJ",
                "descripcion": "Especializada en jóvenes y adicciones. 55 5212 1212.",
                "enlace": "https://www.gob.mx/tramites/ficha/atencion-psicologica-a-distancia-en-salud-mental-y-adicciones/CIJ3570",
                "boton": "Ir al sitio"
            }
        ]

    return render_template("resultado.html", puntaje=puntaje_total, nivel=nivel, mensaje=mensaje, recursos=recursos)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')

        conn = sqlite3.connect('mindcheck.db')
        cursor = conn.cursor()
        cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
        fila = cursor.fetchone()
        conn.close()

        if fila and check_password_hash(fila[0], contraseña):
            session['usuario'] = usuario
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('ver_mensajes'))
        else:
            flash('Credenciales inválidas.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('index'))

@app.route('/mensajes')
def ver_mensajes():
    if 'usuario' not in session:
        flash('Debes iniciar sesión para ver los mensajes.', 'warning')
        return redirect(url_for('login'))

    pagina = request.args.get('page', default=1, type=int)
    por_pagina = 5
    offset = (pagina - 1) * por_pagina
    busqueda = request.args.get('buscar', default='', type=str).strip()

    conn = sqlite3.connect('mindcheck.db')
    cursor = conn.cursor()

    parametros = ()
    query_base = 'FROM mensajes'
    where_clause = ''

    if busqueda:
        where_clause = ' WHERE nombre LIKE ? OR correo LIKE ?'
        parametros = (f'%{busqueda}%', f'%{busqueda}%')

    # Obtener mensajes filtrados
    cursor.execute(f'SELECT id, nombre, correo, texto, fecha {query_base}{where_clause} ORDER BY id DESC LIMIT ? OFFSET ?', (*parametros, por_pagina, offset))
    mensajes = cursor.fetchall()

    # Contar total filtrado
    cursor.execute(f'SELECT COUNT(*) {query_base}{where_clause}', parametros)
    total_mensajes = cursor.fetchone()[0]
    conn.close()

    total_paginas = (total_mensajes + por_pagina - 1) // por_pagina

    return render_template(
        'mensajes.html',
        mensajes=mensajes,
        pagina=pagina,
        total_paginas=total_paginas,
        busqueda=busqueda
    )

@app.route('/exportar-mensajes')
def exportar_mensajes():
    if 'usuario' not in session:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('login'))

    conn = sqlite3.connect('mindcheck.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, correo, texto, fecha FROM mensajes ORDER BY id DESC')
    mensajes = cursor.fetchall()
    conn.close()

    output = []
    header = ['Nombre', 'Correo', 'Mensaje', 'Fecha']
    output.append(header)
    output.extend(mensajes)

    # Crear respuesta CSV
    response = make_response()
    writer = csv.writer(response)
    for row in output:
        writer.writerow(row)

    response.headers['Content-Disposition'] = 'attachment; filename=mensajes.csv'
    response.headers['Content-Type'] = 'text/csv'
    return response

@app.route('/eliminar-mensaje/<int:id>')
def eliminar_mensaje(id):
    if 'usuario' not in session:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('login'))

    conn = sqlite3.connect('mindcheck.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM mensajes WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    flash('Mensaje eliminado correctamente.', 'success')
    return redirect(url_for('ver_mensajes'))

@app.route('/guardar-mensaje', methods=['POST'])
def guardar_mensaje():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    texto = request.form.get('mensaje')
    fecha = datetime.now().strftime('%d/%m/%Y %H:%M')

    conn = sqlite3.connect('mindcheck.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mensajes (nombre, correo, texto, fecha) VALUES (?, ?, ?, ?)',
                   (nombre, correo, texto, fecha))
    conn.commit()
    conn.close()

    flash('Gracias por tu mensaje. Lo hemos recibido.', 'success')
    return redirect(url_for('contacto'))



if __name__ == '__main__':
    app.run(debug=True)
    
