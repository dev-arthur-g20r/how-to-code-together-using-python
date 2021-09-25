import os
def hms(s):
	hours = s // 3600
	seconds = s % 3600
	minutes = seconds // 60
	seconds = seconds % 60
	print(hours,":",minutes,":",seconds)
	return
secs = int(input("Number of seconds to convert to H:M:S: "))
hms(secs)
os.system("pause")