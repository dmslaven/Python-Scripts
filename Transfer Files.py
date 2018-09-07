#written in Python 3.7
#Purpose: Check if files are in a folder, then transfer all those files to new location

import os
import shutil
import time

source = "" #path of source file
destination = "" #path of destination folder
time = 10 #time in seconds

while True:
    if len(os.listdir(source)) == 0: #check if length of items in folder
        print("empty")
    else:
        print("Not Empty")
        files = os.listdir(source)
        for f  in files: #loop through each file
            f = source + '\\' + f #set variable to file path. (Needed as shutil doesn't see the file without the path)
            shutil.move(f,destination) #move file to new location

    time.sleep(time) #pause in seconds before checking again
