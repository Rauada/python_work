cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print('audi' in cars)
print('mercedes' in cars)

new_car = 'ford'
if new_car not in cars:
	print('Car not found')