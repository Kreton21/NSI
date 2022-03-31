import csv
from collections import OrderedDict
import json
f=open("/home/kreton/Documents/coding/NSI/scripts python/CSV/notes.csv")
d=open("/home/kreton/Documents/coding/NSI/scripts python/CSV/notes2.csv")
table=list(csv.DictReader(d,delimiter=","))
table2=list(csv.DictReader(f,delimiter=","))
tables=table+table2

anglais=[e["Nom"] for e in tables if int(e["Anglais"])>8]
print(anglais)