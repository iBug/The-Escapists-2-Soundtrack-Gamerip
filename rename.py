#!/usr/bin/python3

import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
idir = os.path.join(os.getcwd(), "mp3")
odir = os.path.join(os.getcwd(), "The Escapists 2")

with open("select.csv", "r") as f:
    reader = csv.reader(f)
    for _, num, code, name in reader:
        num = num.strip()
        code = code.strip()
        name = name.strip()
        if code == "?" or name == "?":
            continue
        os.symlink(os.path.join("..", "mp3", f"{num}.mp3"), os.path.join(odir, f"{name}.mp3"))
