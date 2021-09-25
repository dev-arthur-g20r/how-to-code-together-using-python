import os
import math
money = float(input("Money: $"))
dollars = int(math.floor(money / 1))

money = money - dollars

quarter = int(math.floor(money / 0.25))
money = money - (quarter * 0.25)

dime = int(math.floor(money / 0.10))
money = money - (dime * 0.10)

nickel = int(math.floor(money / 0.05))
money = money - (nickel * 0.05)

penny = int(round(money * 100))

print("Dollars: ",dollars)
print("Quarters: ",quarter)
print("Dimes: ",dime)
print("Nickels: ",nickel)
print("Pennies: ",penny)
os.system("pause")