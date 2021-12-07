from flask import Flask, render_template, redirect, request, Blueprint
from models.booking import Booking


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

