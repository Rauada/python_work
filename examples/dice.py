from random import randint

class Die:
	"""A simple attempt to model a die."""
	def __init__(self,sides=6):
		"""Initialize attributes to describe a die."""
		self.sides = sides

	def roll_die(self):
		print(randint(1,self.sides))