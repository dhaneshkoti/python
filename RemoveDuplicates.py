def remove_duplicates(list1):
	s=set()
	for i in list1:
		s.add(i)
	l3=list(s)
	return sorted(l3)
a=input("list of elements (separated by spaces): ").split()
list1=list(a)
l2=remove_duplicates(list1)
print(l2)
