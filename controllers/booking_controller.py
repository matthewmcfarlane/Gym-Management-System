from flask import Flask, render_template, redirect, request, Blueprint
from models.booking import Booking

import repositories.fitness_class_repository as fcr
import repositories.member_repository as member
import repositories.booking_repository as booking_repository


bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", current_page='Bookings', bookings=bookings, title='Bookings')


@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")



@bookings_blueprint.route('/bookings/add')
def new_booking():
    fitness_classes = fcr.select_all()
    members = member.select_all()
    return render_template("/bookings/add.html", title='Add Booking', current_page='Add New Booking', fitness_classes=fitness_classes, members=members)

@bookings_blueprint.route('/bookings', methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    fitness_class_id = request.form['fitness_class_id']
    mem = member.select(member_id)
    fitness_class = fcr.select(fitness_class_id)
    booking = Booking(mem, fitness_class)
    booking_repository.save(booking)
    return redirect('/bookings')
