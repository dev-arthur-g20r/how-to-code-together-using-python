#!/usr/bin/python

import os

def checkIfRightTriangle(hypotenuse,leg1,leg2):
	csquare = float(hypotenuse) ** 2
	asquare = float(leg1) ** 2
	bsquare = float(leg2) ** 2
	sum = float(asquare) + float(bsquare)
	if (float(csquare) == float(sum)):
		print "Right Triangle"
	else:
		print "Not a right triangle"
	return
	
c = raw_input("c = ")
a = raw_input("a = ")
b = raw_input("b = ")
checkIfRightTriangle(float(c),float(a),float(b))

os.system("pause")