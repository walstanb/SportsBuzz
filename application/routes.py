from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date
from math import floor

@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html") 

@app.route("/schedule", methods=['GET','POST'])
@app.route("/schedule/<id>", methods=['GET', 'POST'])
def schedule(id=0):
    
    skips=0
    pages= int()
    pagecounter = int(id)
    if pagecounter>=0:
        count = db.team_schedule.count()
        pages=floor(count/10)
        skips = 10 * pagecounter
        if skips>=count:
            pagecounter-=1
            skips=10* pagecounter
            flash("No more data")
    elif pagecounter< 0:
        pagecounter=0
        skips=0
        flash("First Page. No previous data found")

    results = db.team_schedule.find().skip(skips).limit(11)
    
    
    print (pages)
    return render_template("football.html", results = results,i=pagecounter,p=pages)


