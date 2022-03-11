import csv
from collections import OrderedDict
import json
f=open("/home/alexandru/Alexandru/NSI/scripts python/CSV/notes.csv",encoding="utf8")
table=list(csv.DictReader(f,delimiter=","))

def convert(T):
    R=json.loads(json.dumps(T))
    print(R)
    for i in R:
        for j in i:
            if j=="Nom":
                continue
            R[i][j]=int(R[i][j])
    print(R)

convert(table)