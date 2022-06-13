# Make an empty list for storing aliens.
aliens = []

# Make 10 green aliens.
for alien_number in range(10):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)

# Change first 3 aliens to yellow.
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# Change aliens colors: green to yellow and yellow to red.
for alien in aliens[:7]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Show all aliens.
index = 1
for alien in aliens:
	print(f"Alien {index}: {alien}")
	index += 1