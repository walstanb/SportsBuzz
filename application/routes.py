from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date
pagecounter = 0

@app.route("/", methods=['GET', 'POST'])
def index():
    global pagecounter
    skips=0
    number=5
    if (pagecounter+number>1):
        skips = 11 * (pagecounter+number)
        pagecounter += number

    results = db.team_schedule.find().skip(skips).limit(11)
    return render_template("football.html", results = results)


