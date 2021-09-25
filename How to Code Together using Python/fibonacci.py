#!/usr/bin/python

import os

def fibonacciSeq(n):
	first = 0
	second = 1
	print ("Fibonacci Series: ")
	print ("%d\n" % int(first))
	print ("%d\n" % int(second))
	counter = 2
	while int(counter) < int(n):
		next = int(first) + int(second)
		print ("%d\n" % int(next))
		first = int(second)
		second = int(next)
		counter = counter + 1

num = input("Number of numbers in Fibonacci series: ")
fibonacciSeq(int(num))

os.system("pause")