from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

## Configuracion de la BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'nmAdmin'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'NuncaMas'

# Ruta index (landing page)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Ruta contactos (organizaciones y sus contactos)
@app.route('/contactos')
def contactos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM organizacion")
    orgs = cur.fetchall()
    cur.connection.commit()
    cur.close()
    print(orgs)
    return render_template('contactanos.html', orgs=orgs)

# Ruta informate
@app.route('/informate')
def informate():
    return render_template('informate.html')

# Ruta test
@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
