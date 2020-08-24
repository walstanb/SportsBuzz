from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date
pagecounter = 0


@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html") 


@app.route("/schedule", methods=['GET', 'POST'])
def schedule():
    global pagecounter
    skips=0

    form1 = next()
    form = prev()
    if form.on_submit():
        pagecounter-=1
    if form1.on_submit():
        pagecounter+=1
    
    
    skips = 11 * pagecounter
        
    results = db.team_schedule.find().skip(skips).limit(11)
    return render_template("football.html", results = results)


