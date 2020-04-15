#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os
import re
import pandas as pd
# CVS file read using Panda
# usecols use for specificaly select columns
# f"{filename}" is used to transfer filepath
def readMyFile(filename):
    B = pd.read_csv(f"{filename}", usecols=["Integral [abs]"],
                    squeeze=True)  # f"{filename} pass the filenames to the readMyfile function in pandas
    return B


# tkinster GUI is allow user to define the folder path
from tkinter import Tk
from tkinter.filedialog import askdirectory

path = askdirectory(title='Select SBR integration Folder')  # shows dialog box and return the path
print(path)
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

E = []
D = []
F = []
G = []
H = []
for f in files:
    C = readMyFile(f)
    # to obtain only the file name fro the parth
    # file name example 27851-HX958B-20156753ex1.csv
    X = os.path.basename(f)
    # to obatin bath number for polymer (201567753)
    samplenname = re.findall('^[^_]+-[^_]+-([0-9]+)', X)  # will transfer the specific part of file name to list
    # to obtain polymer type from the name (HX959B)
    polymertype = re.findall('^[^_]+-([^_]+)-', X)
    # NMR microsctructure calculation
    BDmoles12 = C[2] / 2
    BDmoles14 = (C[1] - C[2]) / 2
    styrenemoles = C[0] / 5
    totalmass = (BDmoles12 + BDmoles14) * 54 + styrenemoles * 104

    k1 = (styrenemoles * 104 * 100) / totalmass
    k2 = (BDmoles14 * 54 * 100) / totalmass
    k3 = (BDmoles12 * 54 * 100) / totalmass
    H.append(samplenname[0])
    G.append(polymertype[0])
    D.append(k1)
    E.append(k2)
    F.append(k3)

import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Type': G, 'Bath No.': H, 'styrene wt %': D , '1,4 butadiene': E, '1,2 butadiene' : F})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('SBRFSPC.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()


# In[ ]:




