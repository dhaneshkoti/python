f1=input("Enter the name of the first input file: ")
f2=input("Enter the name of the second input file: ")
f3=input("Enter the name of the output file: ")
try:
	with open(f1,"r") as fi1,open(f2,'r') as fi2,open(f3,'w')as of:
		c1=fi1.read()
		c2=fi2.read()
		mc=c1+c2
		of.write(mc)
		print("Merged content:")
		print(mc)
except FileNotFoundError:
	print("One or more input files not found.")
