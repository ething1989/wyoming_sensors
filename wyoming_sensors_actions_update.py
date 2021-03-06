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
size = disk_root[2]
used = disk_root[3]

#g= open("/home/pi/Desktop/cleanup.sh", "a")
#g.write('\n')
#g.write('DAT1=$(date --date=\"${dataset_date} -${date_diff} 2 day\" +%Y-%m-%d)')
#g.write('\n')
#g.write('rm -r /home/pi/Desktop/data/camera/$DAT1*')
#g.write('\n')
#g.write('rm -r /home/pi/Desktop/data/mic/$DAT1*')
#g.write('\n')
#g.write('rm -r /home/pi/Desktop/data/envtl/weather$DAT1*')
#g.write('\n')
#g.write('rm -r /home/pi/Desktop/data/envtl/pmdata$DAT1*')
#g.write('\n')
#g.write('rclone copy /home/pi/Desktop/cleanup.sh campdavisjuara:data')
#g.write('\n')
#g.close()

f= open("/home/pi/logs/logfile.txt","a+")
f.write("  disk space and status:  \r\n")
f.write(current_date_and_time_string)
f.write("\r\n  percent used:  ")
f.write(space)
f.write("\r\n  bytes free:  ")
f.write(used)
f.write("\r\n  bytes used:  ")
f.write(size)
f.write("\r\n  status:  \r\n  all good  \r\n")
f.close()

#os.rmdir("/home/pi/Desktop/data/envtl/Python_SI1145")
#os.rmdir("/home/pi/Desktop/data/envtl/Adafruit_Python_GPIO")
