try:
	x=int(input("Enter the numerator: "))
	y=int(input("Enter the denominator: "))
	result=x/y
	print("Result:",result)
except ZeroDivisionError:
	print("Error: division by zero")
except ValueError as x:
	print("Error: {}".format(x))
print("Execution complete")
