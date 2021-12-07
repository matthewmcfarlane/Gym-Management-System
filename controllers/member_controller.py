from flask import Flask, render_template, redirect, request, Blueprint
from models.fittness_class import FitnessClass

from models.member import Member
import repositories. member_repository as member_repository
import repositories.fitness_class_repository as fcr


members_blueprint = Blueprint("members", __name__)


@members_blueprint.route("/members/add")
def new_member():
    return render_template("members/add.html")

@members_blueprint.route("/members", methods =['POST'])
def create_member():
    first_name      = request.form ['first_name']
    last_name       = request.form ['last_name']
    dob             = request.form ['dob']
    email           = request.form['email']
    membership_type = request.form ['membership_type']
    active          = request.form ['active']
    member = Member(first_name, last_name, dob, email, membership_type, active)
    member_repository.save(member)
    return redirect("/members")

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members, current_page = 'Members')


@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    classes = fcr.fitness_classes(member)
    current_page = f'ID{member.id} - {member.first_name} {member.last_name}'
    return render_template("/members/show.html", member=member, classes=classes, current_page = current_page )

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete_member(id)
    return redirect("/members")
