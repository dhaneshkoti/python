def has_duplicates(list1):
	s=set()
	for i in list1:
		if i in s:
			return "True"
		s.add(i)
	return "False"
a=input("list of elements (separated by spaces): ").split()
l1=list(a)
print(has_duplicates(l1))
