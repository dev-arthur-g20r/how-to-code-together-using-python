import os
def vowelOrConsonant(alphabet):
	vowels = ["A","E","I","O","U","a","e","i","o","u"]
	consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
	if alphabet in vowels:
		print(alphabet,"is a vowel.")
	elif alphabet in consonants:
		print(alphabet,"is a consonant.")
	else:
		print("Sorry! Single-character English alphabets are only allowed.")
letter = input("Alphabet to check if vowel or consonant: ")
vowelOrConsonant(letter)
os.system("pause")