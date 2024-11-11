import geometry
print("Select a shape:")
print("1. Circle\n2. Rectangle\n3. Triangle")
m=int(input("Enter your choice (1/2/3): "))
if m==1:
	x=int(input("Enter the radius of the circle: "))
	geometry.c(x)
elif m==2:
	geometry.r()
elif m==3:
	geometry.tr()
# write your code here

geometry.py
# write your code here
import math
def c(x):
	a=math.pi*x*x
	a1=round(a,2)
	b=2*math.pi*x
	b1=round(b,2)
	print("Circle Area: {0}, Perimeter: {1}".format(a1,b1))
def tr():
	x=int(input("Enter the base of the triangle: "))
	y=int(input("Enter the height of the triangle: "))
	z=(1/2)*x*y
	print("Triangle Area:",z)
	print("Note: Triangle perimeter calculation requires side lengths.")
	a=int(input("Enter the length of side 1: "))
	b=int(input("Enter the length of side 2: "))
	c=int(input("Enter the length of side 3: "))
	p=float(a+b+c)
	print("Triangle Perimeter:",p)
def r():
	x=int(input("Enter the length of the rectangle: "))
	y=int(input("Enter the width of the rectangle: "))
	a=float(x*y)
	b=float(2*(x+y))
	print("Rectangle Area: {0}, Perimeter: {1}".format(a,b))
