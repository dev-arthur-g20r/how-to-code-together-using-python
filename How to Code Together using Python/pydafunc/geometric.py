import os
def geometric(first,terms,ratio):
	i = 0
	while (i < terms):
		print(first)
		first *= ratio
		i += 1
terms = int(input("Number of terms in Geometric Sequence: "))
first_term = int(input("First term: "))
ratio = int(input("Common ratio: "))
geometric(first_term,terms,ratio)
os.system("pause")