from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = os.getenv('MYSQLHOST')
app.config['MYSQL_USER'] = os.getenv('MYSQLUSER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQLPASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQLDATABASE')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQLPORT'))  # make sure the port is an integer
mysql = MySQL(app)

# Ruta index (landing page)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Ruta contactos (organizaciones y sus contactos)
@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    contactos = []
    cur = mysql.connection.cursor()
    cur.execute("select contacto.idContacto, contacto.nombre, apellido, contacto.telefono, contacto.correo, organizacion.nombre, contactoOrg.rol from contacto, contactoOrg, organizacion where contacto.idContacto = contactoOrg.idContacto and contactoOrg.idOrganizacion = organizacion.idOrganizacion")
    contactos = cur.fetchall()
    cur.connection.commit()
    cur.close()
    print(contactos)
    return render_template('contactos.html', contactos=contactos)

@app.route('/organizaciones', methods=['GET', 'POST'])
def organizaciones():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM organizacion")
    orgs = cur.fetchall()
    cur.connection.commit()
    cur.close()

    return render_template('organizaciones.html', orgs=orgs)

# Ruta informate
@app.route('/informate')
def informate():
    return render_template('informate.html')

# Ruta test
@app.route('/test')
def test():
    return render_template('test.html')

# Ruta para responder el test
@app.route('/responderTest')
def responder():
    return render_template('responderTest.html')

# Ruta para mostrar resultados
@app.route('/resultados', methods=['POST', 'GET'])
def resultados():
    if request.method=='GET':
        return "NO PUEDES ENTRAR AQUI ASI"
    else:
        total = 0
        # Con este nivel de violencia se buscan organizaciones apropiadas
        nivel = 0
        for key in request.form:
            total = total + int(request.form[key])
        print(total)
        resultado = ""
        if total <= 20:
            resultado = "No se detectan indicios claros de violencia en la relación. Aun así, se recomienda estar atenta y buscar apoyo si sientes que algo no está bien."
            nivel = 1
        elif total <= 40:
            resultado = "Se identifican señales de violencia en la relación. Es importante buscar apoyo y recursos para enfrentar la situación."
            nivel = 2
        elif total > 40:
            resultado = "Se detecta una situación de violencia grave en la relación. Es urgente buscar ayuda y protección."
            nivel = 3

        #### Falta crear consulta para encontrar organizaciones apropiadas

        return render_template('resultados.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
