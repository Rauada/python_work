def make_sandwich(*ingredients):
	"""Prints a summary of the sandwich that is being ordered."""
	print("The ingredients on your sandwich are:")
	for ingredient in ingredients:
		print(f"- {ingredient.title()}")

make_sandwich('cheddar cheese','pastrami','olives','honey mustard')
