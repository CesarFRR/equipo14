import os
from flask import Flask, render_template, flash, redirect, request, session, url_for
import sqlite3
from sqlite3 import Error
#from formContacto import contactoForm
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import login_required
from flask_login import LoginManager, login_user, logout_user, login_required


app = Flask(__name__)

app.secret_key = os.urandom(24)
error = None
 

@app.route('/')
def index():
    return render_template('login.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "equipo14mintic@gmail.com" and password == "Mintic14E":
            session['username'] = username
            return redirect("/superadmin")

        if username == "profesor@gmail.com" and password == "Mintic14E":
            session['username'] = username
            return redirect("/profesor")


        if not username:
            error = 'Usuario no encontrado...'
            flash(error)
            return render_template('login.html')
        if not password:
            error = 'Contraseña incorrecta...'
            flash(error)
            return render_template('login.html')
        try:
            with sqlite3.connect('src\sprint_uninorte.db') as con:
                cur = con.cursor()
                resultado = cur.execute('SELECT password FROM user WHERE username = ?', [username]).fetchone()   
                if resultado != None:
                    claveHash = resultado[0]
                    if(check_password_hash(claveHash, password)):
                        session['username']=username #creación de la variable de sesion
                        #return redirect(url_for('estudiante'))
                        return redirect('/estudiante')
                    else:
                        error = 'Contraseña incorrecta...'
                        flash(error)
                        return render_template('login.html')
                else:
                    error = 'Usuario no encontrado...'
                    flash(error)
                    return render_template('login.html')
        except Error:
            print(Error)
    #return render_template('estudiante.html')


@app.route('/logout')
def logout():
    
    if "usuario" in session:
        session.clear()
        return render_template('login.html')
        
    else:
        flash("Sesión cerrada")
        return render_template('login.html')
        

@app.route('/estudiante')
#@login_required
def estudiante():
    return render_template('estudiante.html')


@app.route("/superadmin")
def superadmin():
    return render_template("superadmin.html")

@app.route("/profesor")
def profesor():
    return render_template("profesor.html")


if __name__=='__main__':
    app.run(debug=True, port=5000)
