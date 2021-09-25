import os
def count(f,t):
	while (f <= t):
		print(f)
		f += 1
from_n = int(input("Count from: "))
to = int(input("To: "))
count(from_n,to)
os.system("pause")