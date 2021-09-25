import os
def add(x,y):
	sum = x + y
	if (x < 0 and y < 0):
		return sum * -1
	else:
		return sum
x = int(input("x: "))
y = int(input("y: "))
result = add(x,y)
print(result)
os.system("pause")