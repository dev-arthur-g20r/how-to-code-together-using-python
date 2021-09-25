import os;
vowels = ["A","E","I","O","U","a","e","i","o","u"];
consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"];
letter = input("Please enter a letter: ");
if letter in vowels:
	print ("%s is a vowel." % letter);
elif letter in consonants:
	print ("%s is a consonant." % letter);
else:
	print ("Sorry! Single-character English alphabets are the characters to be checked in the program.");
os.system("pause");