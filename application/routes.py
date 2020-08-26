from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date


@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html") 

@app.route("/schedule", methods=['GET','POST'])
@app.route("/schedule/<id>", methods=['GET', 'POST'])
def schedule(id=0):
    
    skips=0
    
    pagecounter = int(id)
    if pagecounter>=0:
        count = db.team_schedule.count()
        skips = 10 * pagecounter
        if skips>=count:
            pagecounter=0
            skips=0
            flash("No more data. Returning to first page")
    elif pagecounter< 0:
        pagecounter=0
        skips=0
        flash("First Page. No previous data found")

    results = db.team_schedule.find().skip(skips).limit(11)
    
    
    
    return render_template("football.html", results = results,i=pagecounter)


