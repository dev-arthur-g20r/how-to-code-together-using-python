import os
res = 0
print("SIMPLE SCIENCE: A Quiz Bee to test your knowledge about yourself.")
print("INSTRUCTION: Just enter the letter (uppercase or lowercase) of your answer. If it's correct, you simply will earn a point, otherwise, you will not earn it, recent points remain.")
print("1. What is the compound for water?")
print("A. H20")
print("B. CO2")
print("C. N2O")
print("D. C6H12O6")
answer = input("Answer: ")
if answer == "A" or answer == "a":
	res = res + 1
	print ("Correct! You got ", res, "point(s) out of 5.")
else:
	print ("Incorrect answer. A is the correct answer. Still", res, " point(s) out of 5.")
print("2. What is the process of forming liquid into gas?")
print("A. Freezing")
print("B. Condensation")
print("C. Evaporation")
print("D. Melting")
answer = input("Answer: ")
if answer == "C" or answer == "c":
	res = res + 1
	print ("Correct! You got ", res, "point(s) out of 5.")
else:
	print ("Incorrect answer. C is the correct answer. Still", res, " point(s) out of 5.")
print("3. We, humans, breathe this out for plants.")
print("A. Oxygen")
print("B. Carbon Dioxide")
print("C. Nitrous Oxide")
print("D. Methane")
answer = input("Answer: ")
if answer == "B" or answer == "b":
	res = res + 1
	print ("Correct! You got ", res, "point(s) out of 5.")
else:
	print ("Incorrect answer. B is the correct answer. Still", res, " point(s) out of 5.")
print("4. Plants breathe this out for humans.")
print("A. Oxygen")
print("B. Carbon Dioxide")
print("C. Nitrous Oxide")
print("D. Methane")
answer = input("Answer: ")
if answer == "A" or answer == "a":
	res = res + 1
	print ("Correct! You got ", res, "point(s) out of 5.")
else:
	print ("Incorrect answer. A is the correct answer. Still", res, " point(s) out of 5.")
print("5. Tearing paper into pieces is what kind of change?")
print("A. Physical Change")
print("B. Chemical Change")
answer = input("Answer: ")
if answer == "A" or answer == "a":
	res = res + 1
	print ("Correct! You got ", res, "point(s) out of 5.")
else:
	print ("Incorrect answer. A is the correct answer. Still", res, " point(s) out of 5.")
if (res <= 5 and res >= 3):
	print("Congratulations! You passed. Keep it up. (",res," out of 5 points)")
else:
	print("Sorry! You may have failed but better awareness and luck next time. (",res," out of 5 points)")
os.system("pause")