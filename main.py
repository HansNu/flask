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
    contactos = []
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("select contacto.idContacto, contacto.nombre, apellido, contacto.telefono, contacto.correo, organizacion.nombre, contactoOrg.rol from contacto, contactoOrg, organizacion where contacto.idContacto = contactoOrg.idContacto and contactoOrg.idOrganizacion = organizacion.idOrganizacion")
        contactos = cursor.fetchall()
    connection.close()
    print(contactos)
    return render_template('contactos.html', contactos=contactos)

@app.route('/organizaciones', methods=['GET', 'POST'])
def organizaciones():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM organizacion")
        orgs = cursor.fetchall()
    connection.close()

    return render_template('organizaciones.html', orgs=orgs)

@app.route('/resultados', methods=['POST', 'GET'])
def resultados():
    if request.method=='GET':
        return "NO PUEDES ENTRAR AQUI ASI"
    else:
        resultado = []
        psicologica = int(request.form["psi1"]) + int(request.form["psi2"])
        resultado.append(int(psicologica))
        fisica = int(request.form["fis1"]) + int(request.form["fis2"])
        resultado.append(int(fisica))
        sexual = int(request.form["se1"]) + int(request.form["se2"])
        resultado.append(int(sexual))
        financial = int(request.form["fin1"]) + int(request.form["fin2"])
        resultado.append(int(financial))
        emocional = int(request.form["emo1"]) + int(request.form["emo2"])
        resultado.append(int(emocional))
        honor = int(request.form["hon1"]) + int(request.form["hon2"])
        resultado.append(int(honor))
        
        print(resultado)

        ### Consultas dependiendo de resultados
        orgs = []
        processed_ids = set()
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            for i in range(len(resultado)):
                if resultado[i] > 0:
                    numV = int(i)+1
                    cursor.execute("SELECT idOrganizacion, organizacion.nombre, tipo, descripcion, ubicacion, telefono, correo, sitio, logo, tiposViolencia.nombre FROM organizacion, orgViolencia, tiposViolencia WHERE idOrganizacion = idOrg AND idViolencia = id AND id = %s", (numV,))
                    a = cursor.fetchall()
                    if a:
                        org_id = a[0][0]
                        if org_id not in processed_ids:
                            processed_ids.add(org_id)
                            orgs.append(a)
        connection.close()
        print(orgs)
        
        return render_template('resultados.html', resultado=resultado, orgs=orgs)

@app.route('/organizacionesAdmin', methods=['GET', 'POST'])
def organizacionesAdmin():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM organizacion")
        orgs = cursor.fetchall()
    connection.close()

    return render_template('organizacionesAdmin.html', orgs=orgs)

@app.route('/orgsCambios/<string:idOrg>', methods=['GET', 'POST']) #Para desplegar página con inputs
def editarAdmin(idOrg):
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM organizacion WHERE idOrganizacion=%s", (idOrg,))
        orgs = cursor.fetchall()
    connection.close()
    org = orgs[0]

    return render_template('orgsEditar.html', org=org) 

@app.route('/orgsEditar/<string:idOrg>', methods=['GET', 'POST'])
def editarOrgs(idOrg):
    if request.method == 'POST':
        nomOrg = request.form['nomOrg']
        tipoOrg = request.form['tipoOrg']
        descOrg = request.form['descOrg']
        telOrg = request.form['telOrg']
        correoOrg = request.form['correoOrg']
        sitioOrg = request.form['sitioOrg']
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("UPDATE organizacion SET nombre=%s, tipo=%s, descripcion=%s, telefono=%s, correo=%s, sitio=%s WHERE idOrganizacion=%s", (nomOrg, tipoOrg, descOrg, telOrg, correoOrg, sitioOrg, idOrg,))
            connection.commit()

            cursor.execute("SELECT * FROM organizacion")
            orgs = cursor.fetchall()
        connection.close()

        return render_template('organizacionesAdmin.html', orgs=orgs)
    else: 
        return "Acceso no valido"

@app.route('/orgsBorrar/<string:idOrg>', methods=['GET', 'POST'])
def borrarOrgs(idOrg): 
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM organizacion WHERE idOrganizacion=%s",(idOrg,))
            connection.commit()

            cursor.execute("SELECT * FROM organizacion")
            orgs = cursor.fetchall()
        connection.close()

        return render_template('organizacionesAdmin.html', orgs=orgs)
    else:
        return "Acceso invalido"

@app.route('/agregarOrg', methods=['GET', 'POST'])
def desplegarCampos(): 
    return render_template('agregarOrgs.html') 

@app.route('/agregarOrgs', methods=['GET', 'POST'])
def nuevaOrg():
    if request.method == 'POST':
        nomOrg = request.form['nomOrg']
        tipoOrg = request.form['tipoOrg']
        descOrg = request.form['descOrg']
        telOrg = request.form['telOrg']
        correoOrg = request.form['correoOrg']
        sitioOrg = request.form['sitioOrg']
        imgOrg = request.form['imgOrg']
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO organizacion (nombre, tipo, descripcion, telefono, correo, sitio, logo) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nomOrg, tipoOrg, descOrg, telOrg, correoOrg, sitioOrg, imgOrg,))
            connection.commit()

            cursor.execute("SELECT * FROM organizacion")
            orgs = cursor.fetchall()
        connection.close()

        return render_template('organizacionesAdmin.html', orgs=orgs)

if __name__ == '__main__':
    app.run(debug=True)

