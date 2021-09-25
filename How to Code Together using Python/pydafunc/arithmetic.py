import os
def arithmetic(first,terms,difference):
	i = 0
	while (i < terms):
		print(first)
		first += difference
		i += 1
terms = int(input("Number of terms in Arithmetic sequence: "))
first_term = int(input("First term: "))
diff = int(input("Common difference: "))
arithmetic(first_term,terms,diff)
os.system("pause")