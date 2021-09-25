import os
fahrenheit = input("Please enter Fahrenheit temperature: ")
diff = float(fahrenheit) - 32
prod = float(diff) * 5
celsius = float(prod) / 9
kelvin = float(celsius) + 273.15
print ("Fahrenheit Temperature = %.2f" % float(fahrenheit))
print ("Celsius Temperature = %.2f" % float(celsius))
print ("Kelvin Temperature = %.2f" % float(kelvin))
os.system("pause")