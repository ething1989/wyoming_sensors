##Keep this first part to continue logging whatever you want by appending onto the existing logfile.txt

import time

timestamp1 = time.strftime("%Y-%m-%d  %H:%M:%S")

f= open("/home/pi/logs/logfile.txt","a+")
f.write("/n Hello idiots, it is " % (timestamp1) )
f.close()

##Add scripts to be run below here.
