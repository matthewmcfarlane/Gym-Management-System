from flask import Flask, render_template, redirect, request, Blueprint

from models.member import Member
import repositories. member_repository as member_repository


members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members, current_page = 'Members')


