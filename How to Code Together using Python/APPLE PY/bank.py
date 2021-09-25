import os
def main():
	cash = 5000
	bank(cash)
def bank(cash):
	print("Choose a number: ")
	print("1 - Withdraw")
	print("2 - Deposit")
	print("3 - Balance Inquiry")
	print("4 - Exit")
	choice = int(input("Number: "))
	if (choice == 1):
		money = float(input("Money to withdraw: "))
		cash -= money
		print("Money successfully withdrawn.")
		bank(cash)
	elif (choice == 2):
		money = float(input("Money to deposit: "))
		cash += money
		print("Money successfully deposited.")
		bank(cash)
	elif (choice == 3):
		print("Balance: Php{0:.02f}".format(cash))
		bank(cash)
	elif (choice == 4):
		exit()
	else:
		print("ERROR: Invalid input")
main()
os.system("pause")