current_users = ['Rafael','Carolina','Philipa','Gilberto','Fernanda']
new_users = ['Rafael', 'Philipa','Carolina','Isabella','Victoria']

# makes a copy of current_users list with all lowercase names
current_users_lowercase = []
for user in current_users:
	current_users_lowercase.append(user.lower())

# checks if new username already exists
for user in new_users:
	if user.lower() in current_users_lowercase:
		print(f'{user} has already been chosen.')
	else:
		print(f'{user} is available.')