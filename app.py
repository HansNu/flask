from flask import Flask, render_template, request
import pymysql
import os

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': os.getenv('MYSQLHOST'),
    'user': os.getenv('MYSQLUSER'),
    'password': os.getenv('MYSQLPASSWORD'),
    'db': os.getenv('MYSQLDATABASE'),
    'port': int(os.getenv('MYSQLPORT'))  # make sure the port is an integer
}

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("select contacto.idContacto, contacto.nombre, apellido, contacto.telefono, contacto.correo, organizacion.nombre, contactoOrg.rol from contacto, contactoOrg, organizacion where contacto.idContacto = contactoOrg.idContacto and contactoOrg.idOrganizacion = organizacion.idOrganizacion")
        contactos = cursor.fetchall()
    connection.close()
    return render_template('contactos.html', contactos=contactos)

@app.route('/organizaciones', methods=['GET', 'POST'])
def organizaciones():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM organizacion")
        orgs = cursor.fetchall()
    connection.close()
    return render_template('organizaciones.html', orgs=orgs)

@app.route('/informate')
def informate():
    return render_template('informate.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/responderTest')
def responder():
    return render_template('responderTest.html')

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
