import tkinter as tk
from tkinter import filedialog
import os

def getFolder():
    folderChosen = filedialog.askdirectory()
    if folderChosen:
        folderNameVariable.set(folderChosen)
        path, dirs, files = next(os.walk(folderChosen))
        file_count = len(files)
        fileCountLabel.config(text="This folder has: " +  str(file_count) + " files")
        print (algorithmVariable.get())
        print (numRowsVariable.get())

def doPack():
    print ("ALGORITHM IS: " + algorithmVariable.get())
    print ("NUM ROWS IS: " + numRowsVariable.get())
    print ("NUM COLS IS: " + numColsVariable.get())
    print ("FOLDERNAME IS " + folderNameVariable.get())

root = tk.Tk()
algorithmList = ["atlasLayout", "staggerPack","staggerPack"]

root.title("Flipbook Packer")
root.geometry("600x600")

# Select Folder Button
selectFolderButton = tk.Button(root, text="Select Folder", fg="white", bg = "#263D42", command=getFolder)
selectFolderButton.grid(row=0,column=1)

# The selected folder
folderNameVariable = tk.StringVar(root)
folderLabel = tk.Label(root,textvariable=folderNameVariable, bg="#A1FFE3")
folderLabel.grid(row=0,column=0)
folderLabel.config(text="No Folder Currently Selected")

# Number of files in this folder
fileCountLabel = tk.Label(root, bg="#FFEE6F")
fileCountLabel.grid(row=0,column=2)
fileCountLabel.config(text="")

# Packing Algorithm Label
algorithmLabel = tk.Label(root, text="Packing Algorithm", bg="#A1FFE3")
algorithmLabel.grid(row=1,column=0)

# Packing Algorithm dropdown 
algorithmVariable = tk.StringVar(root)
algorithmVariable.set(algorithmList[0])
algorithmOpt = tk.OptionMenu(root,algorithmVariable, *algorithmList)
algorithmOpt.grid(row=1,column=1)

# Num Rows Label
numRowsLabel = tk.Label(root,text="Num Rows (if using atlasPack): ", bg="#A1FFE3")
numRowsLabel.grid(row=2,column=0)

# Num Rows Entry
numRowsVariable = tk.StringVar(root, value='0')
numRowsEntry = tk.Entry(root,textvariable=numRowsVariable,justify= 'right')
numRowsEntry.grid(row=2, column=1)

# Num Cols Label
numColsLabel = tk.Label(root,text="Num Cols (if using atlasPack): ", bg="#A1FFE3")
numColsLabel.grid(row=3,column=0)

# Num Cols Entry
numColsVariable = tk.StringVar(root, value='0')
numColsEntry = tk.Entry(root,textvariable=numColsVariable,justify= 'right')
numColsEntry.grid(row=3, column=1)

# Img Format Label
imgFormatLabel = tk.Label(root,text="Image Foramt (Input): ", bg="#A1FFE3")
imgFormatLabel.grid(row=4,column=0)

# Img Format Entry
imgFormatVariable = tk.StringVar(root, value='tif')
imgFormatEntry = tk.Entry(root, textvariable=imgFormatVariable)
imgFormatEntry.grid(row=4, column=1)

# Img Format Label
pilFormatLabel = tk.Label(root,text="Image Foramt (Output): ", bg="#A1FFE3")
pilFormatLabel.grid(row=5,column=0)

# Img Format Entry
pilFormatVariable = tk.StringVar(root, value='tiff')
pilFormatEntry = tk.Entry(root, textvariable=pilFormatVariable)
pilFormatEntry.grid(row=5, column=1)

#Pack button
packButton = tk.Button(root, text="PACK", fg="white", bg = "#263D42", command=doPack)
packButton.grid(row=7,column=1)

root.mainloop()


#canvas = tk.Canvas(root, height=700, width=700, bg = "#263D42")
#canvas.pack()

#frame = tk.Frame(root, bg ="white")
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#openFile = tk.Button(root,text="Open File",padx=10, pady=5, fg="white", bg  = "#263D42", command=addApp)
#openFile.pack()

#runApps = tk.Button(root, text="Run Apps",padx=10, pady=5, fg="white", bg  = "#263D42")

#openFile.pack()
#runApps.pack()

#def addApp():
#    for widget in frame.winfo_children():
#        widget.destroy()
#    filename = filedialog.askopenfilename(initialdir="/", title="select File",
#                                          filetypes = (("executables", "*.exe"), ("all files", "*.*")))
#    apps.append(filename)
#    print (apps)
#    for app in apps:
#            label = tk.Label(frame, text = app, bg="gray")
#            label.pack()