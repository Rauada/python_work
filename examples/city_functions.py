def get_formatted_city(city,population,country):
	"""Generate a neatly formatted city name"""
	full_name = f"{city}, {country} - population {population}"
	return full_name.title()