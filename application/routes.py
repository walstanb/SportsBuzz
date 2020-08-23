from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date


@app.route("/", methods=['GET', 'POST'])
def index():
    player_stats=[]
    [player_stats.append(x) for x in db.Epl_player_img.find()]
    teamdict={}
    for x in player_stats:
        if x['Club'] not in teamdict.keys():
            teamdict[x['Club']]="f"+str(id(x['Club']))
    
    return render_template("playerstats-football.html",player_stats=player_stats,teamdict=teamdict)



