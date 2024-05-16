from flask import Flask, request, render_template, redirect, url_for
from m_tasks import add_task, get_task

app = Flask(__name__)
@app.route("/")
def home():
    tareas = get_task()
    return render_template('index.html', lista_tareas = tareas)

@app.route("/add_text", methods=["POST", "GET"])
def AddText():
    if request.method == "POST":
        texto_recibido = request.form["tarea"]
        add_task(texto_recibido)
        return redirect(url_for('home'))
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run()