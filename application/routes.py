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

@app.route("/football_teams", methods=['GET', 'POST'])
@app.route("/football_teams/<tab>", methods=['GET', 'POST'])
def football_teams(tab="leagues"):
    player_stats=[]
    if tab=="leagues":
        [player_stats.append(x) for x in db.epl20playerdata.find()]
    elif tab=="international":
        [player_stats.append(x) for x in db.epl20playerdata.find()]
    teamdict={}
    for x in player_stats:
        if x['Club'] not in teamdict.keys():
            teamdict[x['Club']]="f"+str(id(x['Club']))
    rp=list(teamdict.keys())
    teamz=rp[0]
    
    return render_template("playerstats-football.html",player_stats=player_stats, teamdict=teamdict, teamz=teamz, tab=tab)

