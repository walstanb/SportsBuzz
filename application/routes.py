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
    '''
    if(id == '-1'):
        pagecounter -= 1
    if(id == '1'):
        pagecounter += 1
    '''
    pagecounter = int(id)
    print(pagecounter)
    count = db.team_schedule.objects.count()
    skips = 11 * pagecounter
    results = db.team_schedule.find().skip(skips).limit(11)
    
    if(skips > count):
        pagecounter = 0
        skips = 0
    
    return render_template("football.html", results = results,i=int(id))


