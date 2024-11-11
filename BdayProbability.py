def same_birthday(n):
	pd=1.0
	for i in range(n):
		pd*=(365-i)/365.0
	p_same=1-pd
	return p_same
n=int(input("No of Students: "))
print("Probability of at least one matching birthday: %.4f"%(same_birthday(n)))
