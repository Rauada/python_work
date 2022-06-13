alien_0 = {'x_position':0, 'y_position':25, 'speed':'fast'}
# print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")


# Items creates a dictionary of keys and values
for k,v in alien_0.items():
	print(f"{k} => {v}")

for keys in alien_0.keys():
	print(keys.title())

for key in sorted(alien_0.keys()):
	print(f"The key is: {key.title()}")


for value in alien_0.values():
	print(f"The value is: {value}")