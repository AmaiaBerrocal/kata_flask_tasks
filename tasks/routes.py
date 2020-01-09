from tasks import app
from flask import render_template, request, url_for, redirect
from tasks.forms import TaskForm

import csv

DATOS = './data/tareas.dat'

@app.route("/")
def index():
    fTareas = open(DATOS, 'r')
    csvreader = csv.reader(fTareas, delimiter=',', quotechar= '"')

    datos = []
    for linea in csvreader:
        datos.append(linea)
    
    fTareas.close()
    return render_template("index.html", tareas = datos)
    
@app.route("/newtask", methods=['GET', 'POST'])
def newtask():
    form = TaskForm(request.form)

    if request.method == 'GET':
        return render_template('task.html', form = form)
    
    if form.validate():
        fdatos = open(DATOS, 'a')
        csvwriter = csv.writer(fdatos, delimiter=',', quotechar= '"')

        title = request.values.get('title')
        desc = request.values.get('description')
        date = request.values.get('date')

        csvwriter.writerow([title, desc, date])

        fdatos.close()
        return redirect(url_for('index'))
    else:
        return render_template("task.html", form=form)
    

    
   