#  this python program is write By  Rajith Arachchige (NMR Scientist at Bridgestone Advance Analytical Lab)  to calcuate SBR microstrcture
# this program will allow to process SBR data in highthroughupt fashion
import os
import re
import pandas as pd
# tkinster GUI is allow user to select multiple files
from tkinter import *
from tkinter.ttk import *
# import messagebox class from tkinter
from tkinter import messagebox
# importing askopenfile function
from tkinter.filedialog import askopenfilenames
# importing askdirectory function
from tkinter.filedialog import askdirectory
# variable lists used in the program
files = []
E = []
D = []
F = []
G = []
H = []
y = []

# CVS file read using Panda
# usecols use for specificaly select columns
# f"{filename}" is used to transfer filepath
def readMyFile(filename):
    B = pd.read_csv(f"{filename}", usecols=["Integral [abs]"], squeeze=True)  # f"{filename} pass the filenames to the readMyfile function in pandas
    return B

# This function will allow rwa data folder
# then function go through the folder and read all the .cvs file in to list
def open_folder():
    path = askdirectory(title='Select SBR integration Folder')  # shows dialog box and return the path
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
# This function will allow user to select specific files they want to process
# then the  files will be added into a list
def open_file():
    file = askopenfilenames(parent = root, title="Choose files for Analysis")


    for fname in file:
        files.append(os.path.join(fname))
#        files.append(os.path.split(fname)[1])

    return files

# SBR microstructure calculation
def sbr():
    for f in files:
        C = readMyFile(f)
        X = os.path.basename(f)
        # to obatin bath number for polymer (201567753)
        samplenname = re.findall('^[^_]+-[^_]+-([0-9]+)', X)  # will transfer the specific part of file name to list
        # to obtain polymer type from the name (HX959B)
        polymertype = re.findall('^[^_]+-([^_]+)-', X)
        # NMR microsctructure calculation
        BDmoles12 = C[2] / 2
        BDmoles14 = (C[1] -BDmoles12 ) / 2
        styrenemoles = C[0] / 5
        totalmass = (BDmoles12 + BDmoles14) * 54 + styrenemoles * 104

        k1 = (styrenemoles * 104 * 100) / totalmass
        k2 = (BDmoles14 * 54 * 100) / totalmass
        k3 = (BDmoles12 * 54 * 100) / totalmass
        H.append(samplenname[0])
        G.append(polymertype[0])
        #D.append(k1)
        #E.append(k2)
        #F.append(k3)
        # "{:.2f}".format(k1) is used to limit the number of decimal points to two
        D.append("{:.2f}".format(k1))
        E.append("{:.2f}".format(k2))
        F.append("{:.2f}".format(k3))

# save the excel file
def save1():
    # Obtain LIMS order number( this will assume all the selected files have same LIMS order number
    y= re.findall('(^[^_]+)-[^_]+-', os.path.basename(files[0]))
#    path1 = askdirectory(title='Select Save Folder')
    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Polymer Type': G, 'Lot No.': H, 'styrene wt %': D, '1,4 butadiene': E, '1,2 butadiene': F})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # for the file name, LIMS order number is used
    writer = pd.ExcelWriter(y[0]+'-SBR-no-block-Anlysis' + '.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Set the column width and format.
    # 0,4 formating is apply for first 5 columns
    # 15 column width
    worksheet.set_column(0, 4, 15)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
# The main program starts

if __name__ == "__main__":
    # Creat a GUI window
    root = Tk()
    # Set the background Colour
    root.configure(background = "light blue")
    # Set the GUI title
    root.title("SBR Microstructure Analysis (AAL)")
    root.geometry('600x175')
    masage1 = Label (root, text = "Welcome to SBR Microstructure Analysis", foreground="black", font="Helvetica 12 bold",background = "light blue")
    masage1.grid(row =0, column =2)
    masage1 = Label (root, text = "Develop by Advanced Analytical Laboratory at Bridgestone", foreground="black", font="Helvetica 6 bold ",background = "light blue")
    masage1.grid(row =1, column =2)
    masage2 = Label (root, text = "please chose the folder", font="Helvetica 8 bold", background = "light blue")
    masage2.grid(row =2, column =1)
    masage3 = Label (root, text = "please chose files",font="Helvetica 8 bold", background = "light blue")
    masage3.grid(row =2, column =3)
    # Creat file select button
    btn = Button(root, text='file', command=lambda: open_file())
    #file select button position. grid command is use to position the button
    btn.grid(row = 3, column =3)
    #Creat folder select button
    btn1 = Button(root, text='folder', command=lambda: open_folder())
    btn1.grid(row = 3, column =1)
    masage4 = Label(root, text="Calculate Microstructure",foreground="blue", font="Helvetica 10 bold", background = "light blue")
    masage4.grid(row=4, column=2)
    # Creat sbr microstrture calclation button
    btn2 = Button(root, text='Cal', command=lambda: sbr())
    btn2.grid(row=5, column=2)
    masage5 = Label(root, text="Save Microstructure Analysis Summary Sheet",foreground="red",font="Helvetica 10 bold", background = "light blue")
    masage5.grid(row=6, column=2)
    # save button
    btn3 = Button(root, text='Save', command=lambda: save1())
    btn3.grid(row=7, column=2)
    root.mainloop()







