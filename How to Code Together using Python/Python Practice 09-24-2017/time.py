import os
def timeCheck(s):
	hours = s // 3600
	secs = s % 3600
	minutes = secs // 60
	seconds = secs % 60
	print(hours,":",minutes,":",seconds)
sec = int(input("Number of seconds: "))
timeCheck(sec)
os.system("pause")