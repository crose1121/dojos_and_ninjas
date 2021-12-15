from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja 

@app.route('/ninja/new')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('create_ninja.html', dojos=dojos)


@app.route('/ninja/create/', methods=['POST'])
def create_ninja():
    new_ninja_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }

    new_ninja = Ninja.create_ninja(new_ninja_data)

    return redirect('/')
