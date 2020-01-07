from tasks import app
from flask import render_template, request, url_for, redirect
import csv

@app.route("/")
def index():
    fTareas = open('./data/tareas.dat', 'r')
    csvreader = csv.reader(fTareas, delimiter=',')

    datos = []
    for linea in csvreader:
        datos.append(linea)
    
    fTareas.close()
    return render_template("index.html", tareas = datos)
    
@app.route("/newtask", methods=['GET', 'POST'])
def newtask():
    if request.method == 'GET':
        return render_template('task.html')
    
    if request.method == 'POST': 
        fdatos = open('./data/tareas.dat', 'a')
        csvwriter = csv.writer(fdatos, delimiter=',', quotechar= '"')

        title = request.values.get('title')
        desc = request.values.get('desc')
        date = request.values.get('date')

        csvwriter.writerow([title, desc, date])

        fdatos.close()
        return redirect(url_for('index'))
    
    
   