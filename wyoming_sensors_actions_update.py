##Keep this first part to continue logging whatever you want by appending onto the existing logfile.txt

import datetime

current_date_and_time = datetime.datetime.now()
current_date_and_time_string = str(current_date_and_time)

f= open("/home/pi/logs/logfile.txt","a+")
f.write("/n Hello idiots, it is " current_date_and_time_string)
f.close()

##Add scripts to be run below here.
