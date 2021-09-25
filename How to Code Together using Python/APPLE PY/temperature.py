import os
print("Choose temperature to convert:")
print("C - Celsius")
print("F - Fahrenheit")
print("K - Kelvin")
choice = input("Temperature to convert: ")
if (choice == "C" or choice == "c"):
	celsius = float(input("Celsius temperature: "))
	fahrenheit = c * 1.8 + 32
	kelvin = celsius + 273.15
	print("Fahrenheit temperature: {0:.03f}".format(fahrenheit))
	print("Kelvin temperature: {0:.03f}".format(kelvin))
elif (choice == "F" or choice == "f"):
	fahrenheit = float(input("Fahrenheit temperature: "))
	celsius = (fahrenheit - 32) / 1.8
	kelvin = (fahrenheit + 459.67) / 1.8
	print("Celsius temperature: {0:.03f}".format(celsius))
	print("Kelvin temperature: {0:.03f}".format(kelvin))
elif (choice == "K" or choice == "k"):
	kelvin = float(input("Kelvin temperature: "))
	celsius = kelvin - 273.15
	fahrenheit = kelvin * 1.8 - 459.67
	print("Celsius temperature: {0:.03f}".format(celsius))
	print("Fahrenheit temperature: {0:.03f}".format(fahrenheit))
else:
	print("Invalid input")
os.system("pause")