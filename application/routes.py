from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date
pagecounter = 0


@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html") 


@app.route("/schedule/<id>", methods=['GET', 'POST'])
def schedule(id=1):
    global pagecounter
    skips=0
    if(id == '-1'):
        pagecounter -= 1
    elif(id == '1'):
        pagecounter += 1
    print(pagecounter)
    count = db.team_schedule.objects.count()
    skips = 11 * pagecounter
    results = db.team_schedule.find().skip(skips).limit(11)
    
    if(skips > count):
        pagecounter = 0
        skip = 0
    
    return render_template("football.html", results = results)


