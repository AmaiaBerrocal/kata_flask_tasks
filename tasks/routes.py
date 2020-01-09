from tasks import app
from flask import render_template, request, url_for, redirect
from tasks.forms import TaskForm, ProcessTaskForm

import csv
from datetime import date

DATOS = './data/tareas.dat'
COPIA = './data/copia.dat'

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
    
@app.route("/processtask", methods=['GET', 'POST'])
def processTask():
    form = ProcessTaskForm(request.form)
    if request.method == 'GET':
        fdatos = open(DATOS, 'r')
        csvreader = csv.reader(fdatos, delimiter=",", quotechar='"')

        registroAct = None
        ilinea = 1
        ix = int(request.values.get('ix'))
        for linea in csvreader:
            if ilinea == ix:
                registroAct = linea
                break
            ilinea += 1
        
        if registroAct:
            if registroAct[2]:
                fechaTarea = date(int(registroAct[2][:4]), int(registroAct[2][5:7]), int(registroAct[2][8:]))
            else:
                fechaTarea = None

            accion = ''
            if 'btnModificar' in request.values:
                accion = 'M'

            if 'btnBorrar' in request.values:    
                accion = 'B'

            form = ProcessTaskForm(data={'ix': ix, 'title': registroAct[0], 'description': registroAct[1], 'date': fechaTarea, 'btn': accion})

        return render_template("processtask.html", form=form)  
    
    if form.btn.data == 'B':
        print('borrar registro')
        return redirect(url_for('index'))
    
    if form.btn.data == 'B':    
        if form.validate():
            print("Modificar el fichero")

            original = fopen(DATOS, 'r')
            copia = fopen(COPIA, 'w')

            return redirect(url_for('index'))

        return render_template("processtask.html", form=form) 
