import os
def isPalindrome(s):
	copy = s
	s = s.lower()
	s = s.replace(" ","")
	for i in s:
		if (not i.isalnum()):
			s = s.replace(i,"")
	check = list(s)
	newString = ""
	i = len(check) - 1
	while (i >= 0):
		newString += check[i]
		i -= 1
	if (newString == s):
		return "Palindrome"
	else:
		return "Not a Palindrome"
string = input("Sentence to check if Palindrome: ")
result = isPalindrome(string)
print(result)
os.system("pause")