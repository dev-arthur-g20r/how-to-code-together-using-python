import os
def futurePrincipal(p,a,y):
	a *= 0.01
	for i in range(y):
		p *= (1 + a)
	print("The value of principal in ", y, " years is Php ", p)
	return
principal = float(input("Principal: Php "))
apr = float(input("Annual percentage rate (in percent): "))
years = int(input("Years: "))
futurePrincipal(principal,apr,years)
os.system("pause")