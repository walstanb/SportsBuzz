from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date



@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html") 


@app.route("/football/teams", methods=['GET', 'POST'])
@app.route("/football/teams/<tab>", methods=['GET', 'POST'])
def teambrowser(tab="leagues"):
    player_stats=[]
    [player_stats.append(x) for x in db.epl20playerdata.find()]
    teamdict={}
    for x in player_stats:
        if x['Club'] not in teamdict.keys():
            teamdict[x['Club']]="f"+str(id(x['Club']))
    rp=list(teamdict.keys())
    teamz=rp[0]
    
    return render_template("playerstats-football.html",player_stats=player_stats, teamdict=teamdict, teamz=teamz)



