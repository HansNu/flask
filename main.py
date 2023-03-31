from flask import Flask, render_template, request
import pymysql
import os

app = Flask(__name__)

# app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
# app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_DATABASE_URL'] = 'mysql://root:fzlcof6vvGsTMMyX1EfD@containers-us-west-44.railway.app:7981/railway'
# app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
# app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
# app.config['MYSQL_DB'] = os.environ['MYSQL_DB']

# Ruta index (landing page)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Ruta contactos (organizaciones y sus contactos)
@app.route('/contactos')
def contactos():
    conn = pymysql.connect(unix_socket=app.config['MYSQL_DATABASE_URL'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM organizacion")
    orgs = cur.fetchall()
    conn.close()
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
