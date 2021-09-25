import os
def time(s):
	hours = s // 3600
	sec = s % 3600
	minutes = sec // 60
	secs = sec % 60
	print(hours,":",minutes,":",secs)
seconds = int(input("Number of seconds: "))
time(seconds)
os.system("pause")