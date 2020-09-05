import pymongo

conn = pymongo.MongoClient("mongodb+srv://sbuzzdbuser:rTZqgmtHXhpISrR7@cluster0.60uwm.gcp.mongodb.net/sportsbuzzdb?retryWrites=true&w=majority")
db = conn["sportsbuzzdb"]
'''player_stats=[]
[player_stats.append(x) for x in db.Epl_player_img.find()]
#player_stats = db.Epl_player_img.find()
teams=[]
#print(player_stats)
teamdict={}
for x in player_stats:
    if x['Club'] not in teamdict.keys():
        teamdict[x['Club']]=id(x['Club'])


#print(teamdict)
for team in teamdict.keys():
    print(team)
    for player in player_stats:
        if player['Club']==team:
            print(player['Image'])
            #print('\t'+player['Name'])
#print(teams)'''

'''
tab="leagues"
league=" Spain Primera Division (1)"
teams=[]
leaguedict={}
[teams.append(x) for x in db.teamtournamentrelation.find()]
#print(teams)

teamdict={}
for x in teams:
    if x['league_name'] == league:
        teamdict[x['team_name']]="id"+str(x['team_id'])

for x in teams:
    if x['league_name'] not in teamdict.keys():
        leaguedict[x['league_name']]="id"+str(id(x['league_name']))


player_stats=[]
for teamid in teamdict.values():
    [player_stats.append(x) for x in db.fifa20playerdata.find({"Club ID": teamid})]

#print(leaguedict)'''

#leagueid="id-3986502157215016196"



teams=[]
[teams.append(x) for x in db.football_leagues.find()]

leagues=[]
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

#print(leaguedict)
#print(len(leaguedict))


leagueid=list(leaguedict.keys())[1]

teamdict={}
for x in teams: 
    if (str(x['league_id'])) == leagueid:    
        teamdict["id"+str(x['team_id'])]=str(x['team_name'])

'''
Can be used to load all data at the same time

player_stats=[]
for teamid in teamdict.keys():
    #print(teamid)
    [player_stats.append(x) for x in db.fifa20playerdata.find({"Club ID": teamid[2:]})]

print(len(player_stats))
'''

teamid=list(teamdict.keys())[0]
print(teamid,teamdict[teamid])

player_stats=[]
[player_stats.append(x) for x in db.fifa20playerdata.find({"Club ID": teamid[2:]})]


#print(len(player_stats))


'''
for x in player_stats:
    if x['Club'] not in teamdict.keys():
        teamdict[x['Club']]="f"+str(id(x['Club']))

#print(teamdict)
#print(len(teamdict))
    



'''