#!/usr/bin/python3

import csv
import json
import os
import sys

import identify


os.chdir(os.path.dirname(os.path.abspath(__file__)))
indir = os.path.join(os.getcwd(), "wav")


with open("db.txt", "r") as f:
    db = dict([l.strip().split() for l in f])
recognized = {}
with open("ref.csv", "r") as f:
    reader = csv.reader(f)
    for _, num, strid, name in reader:
        num = num.strip()
        strid = strid.strip()
        name = name.strip()
        if strid != "?" or name != f"Unknown - {num}":
            recognized[num] = name


rows = []
for filename in os.listdir(indir):
    num = filename.removesuffix(".wav")
    ident = db.get(num, "?")
    name = recognized.get(num)
    if not name:
        name = identify.identify(num, ident)
    rows.append([num, ident, name])
rows.sort(key=lambda x: (x[1], x[0]))

writer = csv.writer(sys.stdout)
writer.writerow(["number", "identifier", "name"])
writer.writerows(rows)

j = []
for row in rows:
    j.append({
        "number": row[0],
        "id": row[1],
        "name": row[2],
    })
with open("list.json", "w") as f:
    json.dump(j, f, indent=2, ensure_ascii=False)
