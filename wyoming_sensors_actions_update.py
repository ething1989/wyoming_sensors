##Keep this first part to continue logging whatever you want by appending onto the existing logfile.txt

DATE=$(date --date="${dataset_date} -${date_diff} 1 day" +%Y-%m-%d)

f= open("/home/pi/logs/logfile.txt","a+")
f.write("Hello idiots, it is ", $DATE, " \n")
f.close()

##Add scripts to be run below here.
