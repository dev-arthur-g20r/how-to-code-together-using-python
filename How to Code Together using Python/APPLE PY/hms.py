import os
def hms(s):
	hours = s // 3600
	sec = s % 3600
	minutes = sec // 60
	secs = sec % 60
	print(str(hours).zfill(2),":",str(minutes).zfill(2),":",str(secs).zfill(2))
seconds = int(input("Seconds: "))
hms(seconds)
os.system("pause")