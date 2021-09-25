import os
def countVowels(string):
	vowels = ["A","E","I","O","U","a","e","i","o","u"]
	count = 0
	for i in string:
		if i in vowels:
			count += 1
	print("Number of vowels: ", count)
	return
def countConsonants(string):
	consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
	count = 0 
	for i in string:
		if i in consonants:
			count += 1
	print("Number of consonants: ", count)
	return
def countPunctuations(string):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	count = 0 
	for i in string:
		if i in punctuations:
			count += 1
	print("Number of punctuations: ", count)
	return
statement = input("Enter a statement to count its vowels or consonants: ")
countVowels(statement)
countConsonants(statement)
countPunctuations(statement)
os.system("pause")