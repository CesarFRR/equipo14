# venv\Scripts\activate = Para activar el entorno virtual.
# .\app\app.py = Para correr la app.


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ini():
	#return "hola mundo"
    return render_template ("layout.html")

@app.route("/index")
def index():
	#return "hola mundo"
    return render_template ("index.html")

@app.route("/estudiante")
def estudiante():
	#return "hola mundo"
    return render_template ("estudiante.html")

@app.route("/profesor")
def profesor():
	#return "hola mundo"
    return render_template ("profesor.html")


@app.route("/superadmin")
def superadmin():
	#return "hola mundo"
    return render_template ("superadmin.html")


if __name__== "__main__":
	app.run(debug=True, port=5001)