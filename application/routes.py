from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date


@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html") 


@app.route("/football_teams", methods=['GET', 'POST'])
#@app.route("/football_teams/<tab>", methods=['GET', 'POST'])
#@app.route("/football_teams/<tab>/<leagueid>", methods=['GET', 'POST'])
#@app.route("/football_teams/<tab>/<leagueid>/<teamid>", methods=['GET', 'POST'])
def football_teams(tab="leagues", leagueid="id6899066988075347270", teamid="id241"):
    if tab=="leagues":
        teams=[]
        [teams.append(x) for x in db.football_leagues.find()]

        leagues,leaguedict=[],{}
        for x in teams:
            if x['league_name'] not in [y[1] for y in leagues]:
                leagues.append([x['league_id'],x['league_name'],int(x['hits'])])
            else:
                for z in leagues:
                    if z[0] == x['league_id']:
                        z[2]+=int(x['hits'])
        leagues.sort(reverse= True, key = lambda x: x[2])
        leaguedict={x[0]:x[1] for x in leagues} 
        print(leaguedict)

        #leagueid=list(leaguedict.keys())[1]

        teamdict={}
        for x in teams: 
            if (str(x['league_id'])) == leagueid:    
                teamdict["id"+str(x['team_id'])]=str(x['team_name'])

        #teamid=list(teamdict.keys())[1]

        player_stats=[]
        [player_stats.append(x) for x in db.fifa20playerdata.find({"Club ID": teamid[2:]})]

    '''
    Can be used to load all data at the same time

    player_stats=[]
    for teamid in teamdict.keys():
        #print(teamid)
        [player_stats.append(x) for x in db.fifa20playerdata.find({"Club ID": teamid[2:]})]

    print(len(player_stats))
    '''
    return render_template("playerstats-football.html",player_stats=player_stats, teamdict=teamdict, leaguedict=leaguedict, tab=tab)

'''
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

'''
