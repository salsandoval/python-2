import tkinter as tk
from tkinter import filedialog

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

file_path = filedialog.askopenfilename()

print(file_path)

input('press any key to exit')
