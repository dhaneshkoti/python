ogdict={}
for i in range(6):
	a=input("Enter a key (press Enter to stop): ")
	if a== "":
		break
	b=input("Enter a value for '%s': "%(a))
	ogdict[a]=b

print("Original Dictionary:")
print(ogdict)
inverted_dict={}
for a,b in ogdict.items():
	inverted_dict[b]=a
print("Inverted Dictionary:")
print(inverted_dict)
