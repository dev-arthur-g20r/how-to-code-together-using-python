import os
def hms(secs):
	hours = secs // 3600
	minutes = secs % 3600 // 60
	seconds = secs % 3600 % 60
	h = str(hours)
	if (hours < 10 and hours >= 0):
		h = "0" + h
	m = str(minutes)
	if (minutes < 10 and minutes >= 0):
		m = "0" + m
	s = str(seconds)
	if (seconds < 10 and seconds >= 0):
		s = "0" + s
	return "{}:{}:{}".format(h,m,s)
seconds = int(input("Number of seconds: "))
result = hms(seconds)
print(result)
os.system("pause")