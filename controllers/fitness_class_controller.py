from flask import Flask, render_template, redirect, request, Blueprint
from models.fittness_class import FitnessClass

from models.member import Member
import repositories. member_repository as member_repository
import repositories.fitness_class_repository as fcr

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

@fitness_classes_blueprint.route("/fitness_classes/add")
def add_class():
    return render_template("fitness_classes/add.html")

@fitness_classes_blueprint.route("/fitness_classes", methods =['POST'])
def create_class():
    name     = request.form ['name']
    capacity      = int(request.form ['capacity'])
    start_time             = request.form ['start_time']
    duration           = request.form['duration']
    day = request.form ['day']
    active          = request.form ['active']
    fitness_class = FitnessClass(name, capacity, start_time, duration, day, active)
    fcr.save(fitness_class)
    return redirect("/fitness_classes")




@fitness_classes_blueprint.route("/fitness_classes")
def fitness_classes():
    classes = fcr.select_all()
    return render_template("fitness_classes/index.html", current_page = 'Classes', classes=classes, title='Classes')

@fitness_classes_blueprint.route("/fitness_classes/<id>/delete", methods = ['POST'])
def delete_fitness_class(id):
    fcr.delete_class(id)
    return redirect('/fitness_classes')
    
