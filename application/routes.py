from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date


@app.route("/", methods=['GET', 'POST'])
def index():
    results = db.team_schedule.find({"AwayTeam":"Man City"})
    return render_template("index.html", results = results)


