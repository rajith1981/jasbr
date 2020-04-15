import os
import re
import pandas as pd
from tkinter import *
from tkinter.ttk import *
import os
# import messagebox class from tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askdirectory
def readMyFile(filename):
    B = pd.read_csv(f"{filename}", usecols=["Integral [abs]"], squeeze=True)  # f"{filename} pass the filenames to the readMyfile function in pandas
    return B
files = []
E = []
D = []
F = []
G = []
H = []
LIMS = []
X =[]
def open_file():

    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Polymer Type': G, 'Bath No.': H, 'styrene wt %': D, '1,4 butadiene': E, '1,2 butadiene': F})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # for the file name, LIMS order number is used
    # writer = pd.ExcelWriter(str(LIMS[0]) +'-SBR-no-block-Anlysis'+'.xlsx', engine='xlsxwriter')
    writer = pd.ExcelWriter('SBR-no-block-Anlysis.xlsx', engine='xlsxwriter')
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

    file = askopenfilenames( title="Choose files for Analysis")


    for fname in file:
        files.append(os.path.join(fname))
#        files.append(os.path.split(fname)[1])
        return files
    print(files)

def open_folder():
#    files = []
    path = askdirectory(title='Select SBR integration Folder')  # shows dialog box and return the path
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
def sbr():
    for f in files:
        C = readMyFile(f)
        print(f)
        print(C[0])
        print(C[1])
        print("**************************")
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

def save():
    # get the LIMS order number from file name
    #LIMS = re.findall('(^[^_]+)-[^_]+-', X[0])
    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Polymer Type': G, 'Bath No.': H, 'styrene wt %': D, '1,4 butadiene': E, '1,2 butadiene': F})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # for the file name, LIMS order number is used
    #writer = pd.ExcelWriter(str(LIMS[0]) +'-SBR-no-block-Anlysis'+'.xlsx', engine='xlsxwriter')
    writer = pd.ExcelWriter('SBR-no-block-Anlysis.xlsx', engine='xlsxwriter')
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


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.configure(background="light green")

    # set the name of tkinter GUI window
    gui.title("Polymer Analysis (AAL)")

    # Set the configuration of GUI window
    gui.geometry("600x200")

    # Create a Resultant Age Button and attached to calculateAge function
    btn = Button(gui, text='Open', command=lambda: open_file())
    btn.pack(side=TOP, pady=10)
    btn2 = Button(gui, text='folder', command=lambda: open_folder())
    btn2.pack(side=TOP, pady=10)
    btn3 = Button(gui, text='Cal', command=lambda: sbr())
    btn3.pack(side=BOTTOM, pady=10)
    btn4 = Button(gui, text='Save', command=lambda: save())
    btn4.pack(side=BOTTOM, pady=20)
    gui.mainloop()

print(H)