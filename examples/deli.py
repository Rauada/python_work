sandwich_orders = ['pastrami','tuna','pastrami','ham and cheese','carbonara','egg','pastrami']
finished_sandwiches = []

print("The Deli has run out of pastrami.")

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	if sandwich == 'pastrami':
		sandwich_orders.remove('pastrami')
	else:
		print(f"I made your {sandwich.title()} sandwich")
		finished_sandwiches.append(sandwich)

print(finished_sandwiches)