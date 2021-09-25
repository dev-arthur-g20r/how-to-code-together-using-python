import os
def hoursAndMinutes(mins):
	hours = mins // 60
	minutes = mins % 60
	print(hours, " hours, ", minutes, " minutes")
	return
m = int(input("Minutes to convert to hours and minutes: "))
hoursAndMinutes(m)
os.system("pause")