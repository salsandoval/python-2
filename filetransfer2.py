import tkinter 
from tkinter import *
import tkinter.filedialog
import os
import datetime
from datetime import timedelta
import shutil



def pickSourceDir():
    myDir = tkinter.filedialog.askdirectory()
    source_dir.delete(0, END)
    source_dir.insert(0, myDir)

def pickDestDir():
    myDir = tkinter.filedialog.askdirectory()
    destination_dir.delete(0, END)
    destination_dir.insert(0, myDir)

def moveFiles():
    source = source_dir.get()
    destination = destination_dir.get()
    source_files = os.listdir(source)
    for i in source_files:
        file_path = os.path.join(source, i)
        hours_ago_24 = datetime.datetime.now() - timedelta(hours = 24)
        modification_time = os.path.getmtime(file_path)
        date_time_of_file = datetime.datetime.fromtimestamp(modification_time)
        if hours_ago_24 < date_time_of_file:
            shutil.move(source + '/' + i, destination)
            print(i + ' was succesfully transferred.')

m = tkinter.Tk()

m.minsize(750, 150)
m.title("Check Files")

btn_Browse1 = Button(m, text="Browse...", padx=20, command=pickSourceDir)
btn_Browse1.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

source_dir = Entry(m, width=100)
source_dir.grid(row=0, column=1, padx=20, pady=(30, 0), sticky=E)

btn_Browse2 = Button(m, text="Browse...", padx=20, command=pickDestDir)
btn_Browse2.grid(row=1, column=0, padx=(20, 10), pady=(10))

destination_dir = Entry(m, width=100)
destination_dir.grid(row=1, column=1, padx=20, pady=10, sticky=E)

btn_check = Button(text="Check for files...", pady=10, command=moveFiles)
btn_check.grid(row=2, column=0, padx=(20, 10), pady=(0, 15))

btn_close = Button(text="Close Program", pady=10, command=m.destroy)
btn_close.grid(row=2, column=1, padx=20, pady=(0, 15), sticky=E)

m.mainloop()  
                 



  
