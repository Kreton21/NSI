import csv
from collections import OrderedDict
import json
f=open("/home/kreton/Documents/code/NSI/scripts python/CSV/naissance.csv")
d=open("/home/kreton/Documents/code/NSI/scripts python/CSV/notes.csv")
table=list(csv.DictReader(d,delimiter=","))
table=list(csv.DictReader(f,delimiter=","))


print(table)