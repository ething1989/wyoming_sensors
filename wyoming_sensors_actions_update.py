##Keep the first part to continue logging whatever you want by appending onto the existing logfile.txt
##Add scripts to be run below here, and if testing sensors, have the output print into the log file so you know if they are working

import datetime
import os 


def getDfDescription():
    df = os.popen("df -h /")
    i = 0
    while True:
        i = i + 1
        line = df.readline()
        if i==1:
            return(line.split()[0:6])
                                 
def getDf():
    df = os.popen("df -h /")
    i = 0
    while True:
        i = i + 1
        line = df.readline()
        if i==2:
            return(line.split()[0:6])

current_date_and_time = datetime.datetime.now()
current_date_and_time_string = str(current_date_and_time)
description = getDfDescription()
disk_root = getDf()
space = disk_root[4]
size = disk_space[2]
used = disk_space[3]

f= open("/home/pi/logs/logfile.txt","a+")
f.write(current_date_and_time_string)
f.write("  all good  \r\n")
f.write(space)
f.write(size)
f.write(used)
f.close()

