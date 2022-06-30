def make_shirt(text,size='Large'):
	print(f"\nShirt size is {size} and it's message is '{text}'")


def build_person(first_name,last_name,age=None):
	"""Return a dictionary of information about a person."""
	person = {'first':first_name,'last':last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi','hendrix',27)
print(musician)