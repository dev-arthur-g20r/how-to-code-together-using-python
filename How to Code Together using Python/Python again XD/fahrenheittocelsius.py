import os
def fahrenheitToCelsius(f):
	c = ((f - 32) * 5) / 9
	print("Celsius temperature: {0:0.3f}".format(c))
fahrenheit = float(input("Fahrenheit temperature: "))
fahrenheitToCelsius(fahrenheit)
os.system("pause")