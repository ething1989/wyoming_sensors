##Keep the first part to continue logging whatever you want by appending onto the existing logfile.txt
##Add scripts to be run below here, and if testing sensors, have the output print into the log file so you know if they are working

import datetime

current_date_and_time = datetime.datetime.now()
current_date_and_time_string = str(current_date_and_time)

f= open("/home/pi/logs/logfile.txt","a+")
f.write(current_date_and_time_string)
f.write("  hello idiot  \r\n")
f.close()

