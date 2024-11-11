a=input("list of elements (separated by spaces): ").split()
l=list(a)
def is_sorted(l):
	if (l==sorted(l)):
		return "True"
	else:
		return "False"
print(is_sorted(l))
