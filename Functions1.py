def do_twice(f,x):
	for i in range(1,13):
		f(x)
def print_spam(x):
	print(x)
x=input()
do_twice(print_spam,x)
