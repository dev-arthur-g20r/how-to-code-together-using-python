import os
def everyNth(str,n):
	strlist = list(str)
	new = ""
	i = 0
	length = len(str)
	while i < length:
		new += strlist[i]
		i += n
	print(new)
	return
string = input("String: ")
nth = int(input("Every nth: "))
everyNth(string,nth)
os.system("pause")