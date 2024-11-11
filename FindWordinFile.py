def fnn(fn,wtf):
	try:
		with open(fn,'r')as file:
			content=file.read()
			fw=[word.strip() for word in wtf.split(',')]
			wf=[word for word in fw if word in content]
			if wf:
				print("The following words were found in the file:")
				for word in wf:
					print(word)
			else:
				print("None of the specified words were found in the file.")
	except FileNotFoundError:
		print(f"Error: File '{fn}' not found.")
		print("None of the specified words were found in the file.")
fn=input("Enter the name of the file: ")
wtf=input("Enter the words to find (comma-separated): ")
fnn(fn,wtf)
