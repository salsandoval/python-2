import shutil
import os

#set where the source of the files are
source = '/Users/guapo/Desktop/foldera/'

#set the destination path to folderB
destination = '/Users/guapo/Desktop/folderb/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
