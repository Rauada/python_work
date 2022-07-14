class User:
	"""docstring for User"""
	def __init__(self, first_name,last_name,email,password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.login_attempts = 0

	def describe_user(self):
		print(f"User's name is {self.first_name.title()} {self.last_name.title()}")
		print(f"User's email is {self.email}")
		print(f"User's password is {self.password}")

	def greet_user(self):
		print(f"Welcome {self.first_name.title()} {self.last_name.title()}")

	def increment_login_attempts(self):
		"""Increments the value of login attempts by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resets the login attempts counter to 0."""
		self.login_attempts = 0

user_one = User('rafael','auada','auadarafael@gmail.com','password@123')

user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(user_one.login_attempts)
user_one.reset_login_attempts()
print(user_one.login_attempts)		