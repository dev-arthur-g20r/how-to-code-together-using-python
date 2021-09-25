import os
def ftoc(fahrenheit):
	celsius = (fahrenheit - 32) * 5 / 9
	print("Celsius temperature: ", celsius)
	return
f = float(input("Fahrenheit temperature: "))
ftoc(f)
os.system("pause")