from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL, MySQLdb

app=Flask(__name__, template_folder='template')

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='46497253'
app.config['MYSQL_DB']='prueba1'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

#FUNCION LOGIN
@app.route('/acceso-login', methods=["GET","POST"])
def Login():

    if request.method =='POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo=request.form['txtCorreo']
        _password=request.form['txtPassword']

        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE email = %s AND contraseña  = %s',(_correo, _password,))
        acount = cur.fetchone()

        if acount:
            session['logueado'] = True
            session['idusuarios'] = acount['idusuarios']

            return render_template('admin.html')
        else:
            return render_template('formulario.html', mensaje="Usuario/Clave Incorrectos")


if __name__== '__main__':    
    app.secret_key="46497253"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
    
