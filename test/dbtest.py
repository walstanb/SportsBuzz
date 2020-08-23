import pymongo

conn = pymongo.MongoClient("mongodb+srv://sbuzzdbuser:rTZqgmtHXhpISrR7@cluster0.60uwm.gcp.mongodb.net/sportsbuzzdb?retryWrites=true&w=majority")
db = conn["sportsbuzzdb"]
player_stats=[]
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