import os
def ftoc(f):
	c = ((f - 32) * 5) / 9
	print("Celsius Temperature:",c)
fahrenheit = float(input("Fahrenheit temperature: "))
ftoc(fahrenheit)
os.system("pause")