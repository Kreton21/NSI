import csv
from collections import OrderedDict
import json
f=open("/home/kreton/Documents/code/NSI/scripts python/CSV/notes.csv",encoding="utf8")
table=list(csv.DictReader(f,delimiter=","))

def convert(T):
    R=json.loads(json.dumps(T))
    print(R)

convert(table)