#!/usr/bin/python

import os

def weightIdentify(kg):
	result = float(kg) * 2.2
	if (float(result) > 0 and float(result) <= 115):
		print ("%.2f lbs. - Strawweight" % float(result))
		return
	elif (float(result) > 115 and float(result) <= 125):
		print ("%.2f lbs. - Flyweight" % float(result))
		return
	elif (float(result) > 125 and float(result) <= 135):
		print ("%.2f lbs. - Bantamweight" % float(result))
		return
	elif (float(result) > 135 and float(result) <= 145):
		print ("%.2f lbs. - Featherweight" % float(result))
		return
	elif (float(result) > 145 and float(result) <= 155):
		print ("%.2f lbs. - Lightweight" % float(result))
		return
	elif (float(result) > 155 and float(result) <= 170):
		print ("%.2f lbs. - Welterweight" % float(result))
		return
	elif (float(result) > 170 and float(result) <= 185):
		print ("%.2f lbs. - Middleweight" % float(result))
		return
	elif (float(result) > 185 and float(result) <= 205):
		print ("%.2f lbs. - Light Heavyweight" % float(result))
		return
	elif (float(result) > 205 and float(result) <= 265):
		print ("%.2f lbs. - Heavyweight" % float(result))
		return
	elif (float(result) > 265):
		print ("%.2f lbs. - Excessive weight" % float(result))
		return
	else:
		print ("%.2f lbs. - Impossible weight" % float(result))
		return

kgs = input("Weight in kgs.: ")
weightIdentify(float(kgs))

os.system("pause")
