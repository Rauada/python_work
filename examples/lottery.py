from random import choice

series = [1,23,43,54,56,78,3,10,12,'a','b','c','d','e']

chosen_ticket = []
my_ticket = ['b', 78, 'e', 54, 10]
counter = 1
match = True

while match:
	while len(chosen_ticket) <= 4:
		chosen_ticket.append(choice(series))
		
	if chosen_ticket == my_ticket:
		print(f"Your ticket has been chosen after {counter} tries.")
		match = False
	else:
		counter += 1
