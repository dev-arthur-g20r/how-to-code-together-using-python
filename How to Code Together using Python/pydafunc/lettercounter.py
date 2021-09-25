import os
def letterCounter(string):
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	f = 0
	g = 0
	h = 0
	ay = 0
	j = 0
	k = 0
	l = 0
	m = 0
	n = 0
	o = 0
	p = 0
	q = 0
	r = 0
	s = 0
	t = 0
	u = 0
	v = 0
	w = 0
	x = 0
	y = 0
	z = 0
	for i in string:
		if (i == "A" or i == "a"):
			a += 1 
		if (i == "B" or i == "b"):
			b += 1 
		if (i == "C" or i == "c"):
			c += 1 
		if (i == "D" or i == "d"):
			d += 1 
		if (i == "E" or i == "e"):
			e += 1 
		if (i == "F" or i == "f"):
			f += 1 
		if (i == "G" or i == "g"):
			g += 1 
		if (i == "H" or i == "h"):
			h += 1 
		if (i == "I" or i == "i"):
			ay += 1 
		if (i == "J" or i == "j"):
			j += 1 
		if (i == "K" or i == "k"):
			k += 1 
		if (i == "L" or i == "l"):
			l += 1 
		if (i == "M" or i == "m"):
			m += 1 
		if (i == "N" or i == "n"):
			n += 1 
		if (i == "O" or i == "o"):
			o += 1 
		if (i == "P" or i == "p"):
			p += 1 
		if (i == "Q" or i == "q"):
			q += 1 
		if (i == "R" or i == "r"):
			r += 1 
		if (i == "S" or i == "s"):
			s += 1 
		if (i == "T" or i == "t"):
			t += 1 
		if (i == "U" or i == "u"):
			u += 1 
		if (i == "V" or i == "v"):
			v += 1 
		if (i == "W" or i == "w"):
			w += 1 
		if (i == "X" or i == "x"):
			x += 1 
		if (i == "Y" or i == "y"):
			y += 1 
		if (i == "Z" or i == "z"):
			z += 1 
	if (a > 0):
		print("A occurred {} times.".format(a))
	if (b > 0):
		print("B occurred {} times.".format(b))
	if (c > 0):
		print("C occurred {} times.".format(c))
	if (d > 0):
		print("D occurred {} times.".format(d))
	if (e > 0):
		print("E occurred {} times.".format(e))
	if (f > 0):
		print("F occurred {} times.".format(f))
	if (g > 0):
		print("G occurred {} times.".format(g))
	if (h > 0):
		print("H occurred {} times.".format(h))
	if (ay > 0):
		print("I occurred {} times.".format(ay))
	if (j > 0):
		print("J occurred {} times.".format(j))
	if (k > 0):
		print("K occurred {} times.".format(k))
	if (l > 0):
		print("L occurred {} times.".format(l))
	if (m > 0):
		print("M occurred {} times.".format(m))
	if (n > 0):
		print("N occurred {} times.".format(n))
	if (o > 0):
		print("O occurred {} times.".format(o))
	if (p > 0):
		print("P occurred {} times.".format(p))
	if (q > 0):
		print("Q occurred {} times.".format(q))
	if (r > 0):
		print("R occurred {} times.".format(r))
	if (s > 0):
		print("S occurred {} times.".format(s))
	if (t > 0):
		print("T occurred {} times.".format(t))
	if (u > 0):
		print("U occurred {} times.".format(u))
	if (v > 0):
		print("V occurred {} times.".format(v))
	if (w > 0):
		print("W occurred {} times.".format(w))
	if (x > 0):
		print("X occurred {} times.".format(x))
	if (y > 0):
		print("Y occurred {} times.".format(y))
	if (z > 0):
		print("Z occurred {} times.".format(z))

string = input("Sentence: ")
letterCounter(string)
os.system("pause")