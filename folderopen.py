#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv
def readMyFile(filename):
    dates = []
    scores = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row[0])
            

    return dates

from tkinter import Tk
from tkinter.filedialog import askdirectory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv'in file:
            files.append(os.path.join(r, file))

for f in files:
    dates = readMyFile(f)
    b = 3*int(dates[0])
    c = 4*int(dates[1])
    print("*****************")
    print(f)
    print("*****************")
    print(dates)
    print(b)
    print(c)

