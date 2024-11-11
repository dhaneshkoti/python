try:
	n=input("Enter a phone number: ")
	if n.isdigit():
		i=len(n)
		if(i==10):
			print("Phone number is valid.")
		else:
			print("Phone number is invalid.")
	else:
		print("Phone number is invalid.")
except ValueError:
	print("Phone number is invalid.")
s=input("Enter an email address: ")
try:
	x=s.split(".")
	if(x[1]=="com"):
		print("Email address is valid.")
	else:
		print("Email address is invalid.")
except:
	print("Email address is invalid.")
