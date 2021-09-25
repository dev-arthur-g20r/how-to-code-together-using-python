import os
def countOddOrEven(f,t):
	while (f <= t):
		if (f % 2 == 0):
			print(f,"- EVEN")
		else:
			print(f,"- ODD")
		f += 1
from_n = int(input("Count from: "))
to = int(input("To: "))
countOddOrEven(from_n,to)
os.system("pause")