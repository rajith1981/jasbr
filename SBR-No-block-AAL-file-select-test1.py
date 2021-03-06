#  this python program is write By  Rajith Arachchige (NMR Scientist at Bridgestone Advance Analytical Lab)  to calcuate SBR microstrcture
# using this program will allow to process SBR data in highthroughupt fashion
import os
import re
import pandas as pd
# CVS file read using Panda
# usecols use for specificaly select columns
# f"{filename}" is used to transfer filepath
def readMyFile(filename):
    B = pd.read_csv(f"{filename}", usecols=["Integral [abs]"], squeeze=True)  # f"{filename} pass the filenames to the readMyfile function in pandas
    return B


# tkinster GUI is allow user to define the folder path

from tkinter import Tk
from tkinter.filedialog import askdirectory
files = []
def open_folder():
    files = []
    path = askdirectory(title='Select SBR integration Folder')  # shows dialog box and return the path
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))

# tkinster GUI is allow user to select multiple files
from tkinter import *
from tkinter.ttk import *
import os

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfilenames

root = Tk()

root.configure(background = "light green")
root.title("Polymer Analysis (AAL)")
root.geometry('400x200')
#files = []
# This function will be used to open
# file in read mode and only Python files
# will be opened


def open_file():
    files = []
    file = askopenfilenames( title="Choose files for Analysis")


    for fname in file:
        files.append(os.path.join(fname))
#        files.append(os.path.split(fname)[1])

    return files


btn = Button(root, text='file', command=lambda: open_file())
btn.pack(side=TOP, pady=10)
#btn2 = Button(root, text='folder', command=lambda: open_folder())
#btn2.pack(side=TOP, pady=10)
mainloop()

E = []
D = []
F = []
G = []
H = []
for f in files:
    C = readMyFile(f)
    # to obtain only the file name fro the path
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
# "{:.2f}".format(k1) is used to limit the number of decimal points to two
    D.append("{:.2f}".format(k1))
    E.append("{:.2f}".format(k2))
    F.append("{:.2f}".format(k3))
# get the LIMS order number from file name
LIMS = re.findall('(^[^_]+)-[^_]+-', X)

import pandas as pd
p =482020
vname = str(p)
# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Polymer Type': G, 'Bath No.': H, 'styrene wt %': D , '1,4 butadiene': E, '1,2 butadiene' : F})

# Create a Pandas Excel writer using XlsxWriter as the engine.
# for the file name, LIMS order number is used
#writer = pd.ExcelWriter(str(LIMS[0]) +'-SBR-no-block-Anlysis'+'.xlsx', engine='xlsxwriter')
writer = pd.ExcelWriter('SBR-no-block-Anlysis.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
# Set the column width and format.
# 0,4 formating is apply for first 5 columns
# 15 column width
worksheet.set_column(0, 4, 15)
# Close the Pandas Excel writer and output the Excel file.
writer.save()
print(files)





