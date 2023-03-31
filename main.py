from flask import Flask, render_template, request
import pymysql
import os

app = Flask(__name__)

mysql_host = os.environ.get('MYSQLHOST')
mysql_port = os.environ.get('MYSQLPORT')
mysql_user = os.environ.get('MYSQLUSER')
mysql_password = os.environ.get('MYSQLPASSWORD')
mysql_database = os.environ.get('MYSQLDATABASE')

# Ruta index (landing page)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Ruta contactos (organizaciones y sus contactos)
@app.route('/contactos')
def contactos():
    conn = pymysql.connect(
        host=mysql_host,
        port=int(mysql_port),
        user=mysql_user,
        password=mysql_password,
        db=mysql_database,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
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
