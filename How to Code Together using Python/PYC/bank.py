import os
def main():
	cash = 5000
	bank(cash)
def withdraw(cash,money):
	cash -= money
	print("Money successfully withdrawn.")
	return cash
def deposit(cash,money):
	cash += money 
	print("Money successfully deposited.")
	return cash
def balance(cash):
	print("Balance: {0:.02f}".format(cash))
def bank(cash):
	print("1 - Deposit")
	print("2 - Withdraw")
	print("3 - Balance Inquiry")
	print("4 - Exit")
	choice = int(input("Number of choice: "))
	if (choice == 1):
		money = float(input("Amount of money to deposit: "))
		cash = deposit(cash,money)
		bank(cash)
	elif (choice == 2):
		money = float(input("Amount of money to withdraw: "))
		cash = withdraw(cash,money)
		bank(cash)
	elif (choice == 3):
		balance(cash)
		bank(cash)
	elif (choice == 4):
		exit()
	else:
		print("Invalid input.")
main()
os.system("pause")