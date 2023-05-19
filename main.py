from flask import Flask, render_template, request, url_for, redirect, flash
import pymysql
from werkzeug.utils import secure_filename
import os, io
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
mysql = MySQL(app)

MAX_CONTENT_LENGTH = 2 * 1000 * 1000 # Cambiar primer numero por numero de MB desados (1 = 1MB)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

## Configuracion de la BD
# MySQL configurations
db_config = {
    'host': os.getenv('MYSQLHOST'),
    'user': os.getenv('MYSQLUSER'),
    'password': os.getenv('MYSQLPASSWORD'),
    'db': os.getenv('MYSQLDATABASE'),
    'port': int(os.getenv('MYSQLPORT'))  # make sure the port is an integer
}

login_manager = LoginManager()
login_manager.init_app(app)

# Class for Admin
class Admin(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


@login_manager.user_loader
def load_user(admin_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin WHERE id = %s", [admin_id])
    data = cur.fetchone()
    if data is None:
        return None
    cur.close()
    # id, username, and password are the fields from your database
    return Admin(data[0], data[1], data[2])

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
    return render_template('contactos.html', contactos=contactos)

@app.route('/organizaciones')
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
         

        ### Consultas dependiendo de resultados
        orgs = []
        processed_ids = set()
        cur = mysql.connection.cursor()
        # Iterar en cada tipo de violencia
        for i in range(len(resultado)):
            # Si hubo respuestas validas, buscar organizaciones pertinentes
            if resultado[i] > 0:
                numV = int(i)+1
                cur.execute("SELECT idOrganizacion, organizacion.nombre, tipo, descripcion, ubicacion, telefono, correo, sitio, logo, tiposViolencia.nombre FROM organizacion, orgViolencia, tiposViolencia WHERE idOrganizacion = idOrg AND idViolencia = id AND id = %s", (numV,))
                a = cur.fetchall()
                # Si no hay ninguna organizacion registrada con ese tipo de violencia, no agregar tupla vacía
                if a:
                    # Verificar que no se repitan organizaciones
                    org_id = a[0][0]
                    if org_id not in processed_ids:
                        processed_ids.add(org_id)  # Add the ID to the set of processed IDs
                        orgs.append(a)
        
        return render_template('resultados.html', resultado=resultado, orgs=orgs)
    
@app.route("/loginAdmin", methods=["GET","POST"])
def loginAdmin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admin WHERE username = %s", [username])
        data = cur.fetchone()

        if data is None:
            flash("Usuario no existe. Intente de nuevo")
            return redirect(url_for('loginAdmin'))

        admin = Admin(data[0], data[1], data[2])

        cur.close()
        if admin.password != password:
            flash("Contraseña incorrecta. Intente de nuevo")
            return redirect(url_for('loginAdmin'))
        login_user(admin)
        return redirect(url_for('index'))

    return render_template("loginAdmin.html", current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/organizacionesAdmin', methods=['GET', 'POST'])
def organizacionesAdmin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM organizacion")
    orgs = cur.fetchall()
    cur.connection.commit()
    cur.close()

    return render_template('organizacionesAdmin.html', orgs=orgs)

@app.route('/orgsCambios/<string:idOrg>', methods=['GET', 'POST']) #Para desplegar página con inputs
def editarAdmin(idOrg):
    cur = mysql.connection.cursor()
    #idOrg = request.args.get('idOrg')
    cur.execute("SELECT * FROM organizacion WHERE idOrganizacion=%s", (idOrg,))
    cur.connection.commit()
    orgs = cur.fetchall()
    org = orgs[0]
    cur.close()

    return render_template('orgsEditar.html', org=org) #Regresa la bd actualizada



# Ruta para editar info de organizaciones como admin
@app.route('/orgsEditar/<string:idOrg>', methods=['GET', 'POST'])
def editarOrgs(idOrg):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        nomOrg = request.form['nomOrg']
        tipoOrg = request.form['tipoOrg']
        descOrg = request.form['descOrg']
        telOrg = request.form['telOrg']
        correoOrg = request.form['correoOrg']
        sitioOrg = request.form['sitioOrg']
        cur.execute("UPDATE organizacion SET nombre=%s, tipo=%s, descripcion=%s, telefono=%s, correo=%s, sitio=%s WHERE idOrganizacion=%s", (nomOrg,tipoOrg, descOrg, telOrg, correoOrg, sitioOrg, idOrg,))
        cur.connection.commit()

        cur.execute("SELECT * FROM organizacion")
        orgs = cur.fetchall()
        cur.connection.commit()
        cur.close()

        return render_template('organizacionesAdmin.html', orgs=orgs) #Regresa la bd actualizada
    else: 
        return "Acceso no valido"

@app.route('/orgsBorrar/<string:idOrg>', methods=['GET', 'POST']) #Manda del botón borrar de orgsEditar
def borrarOrgs(idOrg): 
    if request.method == 'POST':

        # Borrar imagen asociada con este registro
        cur = mysql.connection.cursor()
        cur.execute("SELECT logo FROM organizacion where idOrganizacion=%s", (idOrg,))
        a = cur.fetchall()
        img = a[0][0]
        filepath = os.path.join(app.root_path, 'static/images', img)
        if os.path.exists(filepath):
            os.remove(filepath)
        

        cur.execute("DELETE FROM organizacion WHERE idOrganizacion=%s",(idOrg,))
        cur.connection.commit()

        cur.execute("SELECT * FROM organizacion")
        orgs = cur.fetchall()
        cur.connection.commit()
        cur.close()

        return render_template('organizacionesAdmin.html', orgs=orgs) #Regresa al inicio con la bd actualizada
    else:
        return "Acceso invalido"

@app.route('/agregarOrg', methods=['GET', 'POST']) #Manda del botón borrar de orgsEditar
def desplegarCampos(): 
    return render_template('agregarOrgs.html') #Regresa al inicio con la bd actualizada

@app.route('/agregarOrgs', methods=['GET', 'POST'])
def nuevaOrg():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        nomOrg = request.form['nomOrg']
        tipoOrg = request.form['tipoOrg']
        descOrg = request.form['descOrg']
        telOrg = request.form['telOrg']
        correoOrg = request.form['correoOrg']
        sitioOrg = request.form['sitioOrg']
        imgOrg = ""

        if 'imgOrg' in request.files:
            file = request.files['imgOrg']
            # Si no se sube arhcivo regrsea arcihvo vacio sin nombre
            if file.filename != '':
                
                # Revisar que el archivo sea del tipo que dice
                if is_image_file(file):
                    # Guardar el archivo con el nombre de su organizacion
                    filename = secure_filename(nomOrg)
                    file.save('./static/images/'+filename)
                    imgOrg = filename
                else:
                    return render_template('agregarOrgs.html', error='noValido')
                    #return("<h1>FORMATO DE IMAGEN NO VALIDO</h1><p>Solo se permiten archivos tipo PNG, JPG O JPEG</p>")

        cur.execute("INSERT INTO organizacion (nombre, tipo, descripcion, telefono, correo, sitio, logo) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nomOrg,tipoOrg, descOrg, telOrg, correoOrg, sitioOrg,imgOrg,))
        cur.connection.commit()

    cur.execute("SELECT * FROM organizacion")
    orgs = cur.fetchall()
    cur.connection.commit()
    cur.close()

    return render_template('organizacionesAdmin.html', orgs=orgs) #Regresa la bd actualizada  

# Leer numeros magicos para detectar verdadero tipo de archivo
def is_image_file(file):
    signature = file.read(4)
    if signature == b'\x89\x50\x4E\x47':
        # Regresar apuntador de lectura al principio del archivo. No hacerlo rompe al archivo
        file.seek(0)
        return 'PNG'
    elif signature == b'\xFF\xD8\xFF\xE0' or signature == b'\xFF\xD8\xFF\xE1':
        file.seek(0)
        return 'JPEG'
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
