import os;
num1 = input("First number = ");
num2 = input("Last number = ");
for num in range(int(num1),int(num2)):
	result = int(num) % 2;
	if (int(result) == 0):
		print ("%d - EVEN" % int(num));
	else:
		print ("%d - ODD" % int(num));
num3 = int(num2);
result2 = int(num3) % 2;
if (int(result2) == 0):
	print ("%d - EVEN" % int(num3));
else:
	print ("%d - ODD" % int(num3));
os.system("pause");		