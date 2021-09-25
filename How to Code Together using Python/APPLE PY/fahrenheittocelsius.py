import os
def fahrenheitToCelsius(f):
	c = ((f - 32) * 5) / 9
	print("Circumference of circle: {0:.03f}".format(c))
fahrenheit = float(input("Fahrenheit temperature: "))
fahrenheitToCelsius(fahrenheit)
os.system("pause")