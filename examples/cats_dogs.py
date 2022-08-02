filenames = ['cats.txt','dogs.txt']

def name_reader(filename):
	try:
		with open (filename,encoding='utf-8') as f:
			content = f.read()
	except FileNotFoundError:
		# print(f"Sorry, the file {filename} does not exist.")
		pass
	else:
		names = content.split()
		for name in names:
			print(name)

for filename in filenames:
	name_reader(filename)