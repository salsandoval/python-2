import tkinter 
from tkinter import *
import shutil
import os


#set where the source of the files are
source = '/Users/guapo/Desktop/hold/'

#set the destination path to folderB
destination = '/Users/guapo/Desktop/receive/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

#root.withdraw()

#root.geometry('100x100')

#btn = Button(root, text = 'Click me!', bd = '5',
             #command = root.destroy)
#btn.pack(side = 'top')
#root.mainloop()

#file_path = filedialog.askopenfilename()

#print(file_path)

#input('press any key to exit')

#src_path = r"C:\Users\guapo\Desktop\receive"
#dst_path = r"C:\Users\guapo\Desktop\hold"
#shutil.move(src_path, dst_path)

def pickSourceDir():
    myDir = tKinter.filedialog.askdirectory()
    source_dir.delete(0, END)
    source_dir.insert(0, myDir)

def pickDestDir():
    myDir = tKinter.filedialog.askdirectory()
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
        date_time_ofTfile = datetime.datetime.fromtimestamp(modification_time)
        if hoirs_ago_24 < date_time_of_file:
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
                 



  
