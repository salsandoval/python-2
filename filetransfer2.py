import tkinter as tk
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

root = tk.Tk()
root.withdraw()

root.geometry('100x100')

btn = Button(root, text = 'Click me!', bd = '5',
             command = root.destroy)
btn.pack(side = 'top')
root.mainloop()

file_path = filedialog.askopenfilename()

print(file_path)

input('press any key to exit')

src_path = r"C:\Users\guapo\Desktop\receive"
dst_path = r"C:\Users\guapo\Desktop\hold"
shutil.move(src_path, dst_path)

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



if __name__ == '__main__':
    
