a=input("number1: ")


if a.isdigit():
	b=int(input("number2: "))
	a=int(a)
	if(b==0):
		print("Zero division")
	else:
		def gcd(a,b):
			if(a==0):
				return b
			else:
				return gcd(b%a,a)
		print("GCD of %d and %d: %d"%(a,b,gcd(a,b)))
else:
	print("Invalid input")
