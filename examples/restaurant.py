class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"\nRestaurant's name is {self.restaurant_name}.")
		print(f"It serves {self.cuisine_type} food.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is now open.")

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type='ice cream'):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an ice cream stand.
		"""
		super().__init__(restaurant_name,cuisine_type='ice cream')
		self.flavors = ['vanilla','mint','chocolate']

	def print_flavors(self):
		"""Print a statement listing all flavors offered."""
		print(f"{self.restaurant_name} serves {self.cuisine_type} and has the following flavors:")
		for flavor in self.flavors:
			print(flavor.title())

bobs = IceCreamStand("Bob's Stand")
bobs.print_flavors()