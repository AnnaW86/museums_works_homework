from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository
import repositories.work_repository as work_repository

works_blueprint = Blueprint("works", __name__)

# INDEX
# GET '/works
@works_blueprint.route("/works")
def works():
    works = work_repository.select_all()
    return render_template("works/index.html", all_works = works)


# NEW
# GET '/works/new'
@works_blueprint.route("/works/new")
def new_works():
    museums = museum_repository.select_all()
    return render_template("works/new.html", all_museums = museums)


# CREATE
# POST '/works'
@works_blueprint.route("/works", methods=['POST'])
def create_work():
    title = request.form['title']
    artist = request.form['artist']
    year = request.form['year']
    museum_id = request.form['museum_id']
    museum = museum_repository.select(museum_id)
    work = Work(title, artist, year, museum)
    work_repository.save(work)
    return redirect("/works")


# SHOW
# GET '/works/<id>'
@works_blueprint.route("/works/<id>")
def show_work(id):
    return render_template("works/show.html", work = work_repository.select(id))

# EDIT
# GET '/works/<id>/edit'
@works_blueprint.route("/works/<id>/edit")
def edit_work(id):
    museums = museum_repository.select_all()
    work = work_repository.select(id)
    return render_template("works/edit.html", all_museums = museums, work = work)

# UPDATE
# PUT '/works/<id>'
@works_blueprint.route("/works/<id>", methods=['POST'])
def update_work(id):
    title = request.form['title']
    artist = request.form['artist']
    year = request.form['year']
    museum_id = request.form['museum']
    museum = museum_repository.select(museum_id)
    work = Work(title, artist, year, museum, id)
    work_repository.update(work)
    return render_template("works/show.html", work = work_repository.select(id))


# DELETE
# DELETE '/works/<id>'
@works_blueprint.route("/works/<id>/delete", methods=['POST'])
def delete_work(id):
    work_repository.delete(id)
    return redirect("/works")



