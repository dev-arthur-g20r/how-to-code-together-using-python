
import os
import locale
locale.setlocale( locale.LC_ALL, 'en_US' )
def property_tax(assessed_val):
	taxable_amt = assessed_val * 0.92
	tax_rate = 1.05
	property_tax = (taxable_amt / 100) * tax_rate
	print("ASSESSED VALUE: Php {}".format(locale.format("%.2f",assessed_val,grouping=True)))
	print("TAXABLE AMOUNT: Php {0:.02f}".format(locale.format("%.2f",taxable_amt,grouping=True)))
	print("TAX RATE per Php 100.00: Php {0:.02f}".format(locale.format("%.2f",tax_rate,grouping=True)))
	print("PROPERTY TAX: Php {0:.02f}".format(locale.format("%.2f",property_tax,grouping=True)))
amount = float(input("Assessed value: "))
property_tax(amount)
os.system("pause")