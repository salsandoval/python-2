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
