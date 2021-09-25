import os
def celsiusToFahrenheit(c):
	f = ((9 / 5) * c) + 32
	print("Fahrenheit temperature: {0:0.3f}".format(f))
celsius = float(input("Celsius temperature: "))
celsiusToFahrenheit(celsius)
os.system("pause")