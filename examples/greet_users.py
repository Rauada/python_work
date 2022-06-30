def greet_users(names):
	"""Print a simple greeting to each user in the list"""
	for name in names:
		msg = f"Hello, {name.title}!"
		print(msg)

usernames = ["carolina,'rafael','philipa']
greet_users(usernames)