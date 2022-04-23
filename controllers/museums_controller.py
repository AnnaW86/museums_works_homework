from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository
import repositories.work_repository as work_repository

museums_blueprint = Blueprint("museums", __name__)

# INDEX
# GET '/museums
@museums_blueprint.route("/museums")
def museums():
    museums = museum_repository.select_all()
    return render_template("museums/index.html", all_museums = museums)

# NEW
# GET '/museums/new'
@museums_blueprint.route("/museums/new")
def new_museum():
    return render_template("museums/new.html")

# CREATE
# POST '/museums'
@museums_blueprint.route("/museums", methods=['POST'])
def create_museum():
    name = request.form['name']
    address = request.form['address']
    museum = Museum(name, address)
    museum_repository.save(museum)
    return redirect("/museums")


# SHOW
# GET '/museums/<id>'
@museums_blueprint.route("/museums/<id>")
def show_museum(id):
    museum = museum_repository.select(id)
    works = museum_repository.select_works(id)
    return render_template("museums/show.html", museum = museum, museum_works = works)


# EDIT
# GET '/museums/<id>/edit'
@museums_blueprint.route("/museums/<id>/edit")
def edit_museum(id):
    museum = museum_repository.select(id)
    return render_template("museums/edit.html", museum = museum)

# UPDATE
# PUT '/museums/<id>'
@museums_blueprint.route("/museums/<id>", methods=['POST'])
def update_museum(id):
    name = request.form['name']
    address = request.form['address']
    museum = Museum(name, address, id)
    museum_repository.update(museum)
    return render_template("museums/show.html", museum=museum_repository.select(id))

# DELETE
# DELETE '/museums/<id>'
@museums_blueprint.route("/museums/<id>/delete", methods=['POST'])
def delete_museum(id):
    museum_repository.delete(id)
    return redirect("/museums")


@museums_blueprint.route("/museums/<id>/delete_works", methods=['POST'])
def delete_museum_works(id):
    museum_repository.delete_museums_works(id)
    return redirect(request.referrer)

@museums_blueprint.route("/museums/<id>/add_to_works", methods = ['POST'])
def add_to_works(id):
    museum = museum_repository.select(id)
    return render_template("museums/add_to_work.html", museum = museum)

@museums_blueprint.route("/museums/<id>/update_works", methods=['POST'])
def update_works(id):
    title = request.form['title']
    artist = request.form['artist']
    year = request.form['year']
    museum = museum_repository.select(id)
    work = Work(title, artist, year, museum)
    work_repository.save(work)
    works = museum_repository.select_works(id)
    return render_template("museums/confirm.html", museum = museum, work = work)
    
    