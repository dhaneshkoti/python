# Type Content here...
class Person:
	def __init__(self,name):
		self.name=name
	def display_info(self):
		print("Name:",self.name)
		print("Subject:",self.subject)
	def display_info1(self):
		print("Name:",self.name)
		print("Subject:",self.subject)
		print("Department:",self.department)
class Teacher(Person):
	def __init__(self,name,subject):
		super().__init__(name)
		self.subject=subject
class Employee(Teacher):
	def __init__(self,name,subject,department):
		super().__init__(name,subject)
		self.department=department
def create_teacher():
	name=input("Enter teacher's name: ")
	subject=input("Enter subject taught: ")
	return Teacher(name,subject)
def create_employee():
	name=input("Enter employee's name: ")
	subject=input("Enter subject taught: ")
	department=input("Enter department: ")
	return Employee(name,subject,department)
def main():
	while True:
		print("1. Create Teacher")
		print("2. Create Employee")
		print("3. Quit")
		c=input("Select an option: ")
		if c=='1':
			teacher=create_teacher()
			teacher.display_info()
		elif c=='2':
			employee=create_employee()
			employee.display_info1()
		elif c=='3':
			break
		else:
			print("Invalid choice.Please enter 1, 2, or 3.")
if __name__ =="__main__":
	main()
