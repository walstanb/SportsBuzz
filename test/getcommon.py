import pandas as pd 

df=pd.read_csv("test/imagesclubs.csv")
team_id = df.team_id
team_idr = df.team_idr
inp=list(team_id)
cmp=list(team_idr)

ls=[]
for r in inp:
    if r not in cmp:
        ls.append(r)

print(ls)
print(len(ls))