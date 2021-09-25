import os
def vowelOrConsonant(letter):
	vowels = ["A","E","I","O","U","a","e","i","o","u"]
	consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
	if (letter in vowels):
		print(letter,"is a vowel.")
	elif (letter in consonants):
		print(letter,"is a consonant.")
	else:
		print("Sorry! Single-character English alphabets are only allowed.")
alphabet = input("Single-character alphabet to check if vowel or consonant: ")
vowelOrConsonant(alphabet)
os.system("pause")