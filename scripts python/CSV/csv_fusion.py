import csv
from collections import OrderedDict
import json
f=open("/home/kreton/Documents/code/NSI/scripts python/CSV/notes.csv")
d=open("/home/kreton/Documents/code/NSI/scripts python/CSV/notes2.csv")
table=list(csv.DictReader(f,delimiter=","))
table2=list(csv.DictReader(d,delimiter=","))


