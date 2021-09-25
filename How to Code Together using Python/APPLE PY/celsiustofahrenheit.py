import os
def celsiusToFahrenheit(c):
	f = (c * (9 / 5)) + 32
	print("Fahrenheit temperature: {0:.03f}".format(f))
celsius = float(input("Celsius temperature: "))
celsiusToFahrenheit(celsius)
os.system("pause")