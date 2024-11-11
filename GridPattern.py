a=int(input("Enter the number of rows: "))
b=int(input("Enter the number of columns: "))
def grid(row,col):
	x=("+ - - - - " * col + "+")
	y=("\n" + "|         "*col + "|")
	return((x+4*y)+"\n")*row+x
print(grid(a,b))
