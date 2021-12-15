from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo 

@app.route('/')
def index():
    all_dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos = all_dojos)

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    new_dojo_data = {
        'name': request.form['dojo_name'],
        'location': request.form['dojo_location']
    }
    Dojo.create_new_dojo(new_dojo_data)
    print(new_dojo_data)
    return redirect('/')

@app.route('/dojo/<int:id>/show')
def show_dojo(id):
    dojo_info = {
        'id':id
    }
    dojo = Dojo.show_dojo_and_ninjas(dojo_info)
    return render_template('dojo_show.html',dojo=dojo)


