# favorite_languages = {
# 	'jen': 'python',
# 	'sarah': 'c',
# 	'edward': 'ruby',
# 	'phil': '',
# 	'carol': 'java',
# 	'hank': '',
# }

# print("List of people taking the poll:")
# # if there is a value, print chosen value, else print message
# for key,value in sorted(favorite_languages.items()):
# 	if value:
# 		print(f"{key.title()} has chosen {value.title()}.")
# 	else:
# 		print(f"{key.title()}, please choose your favorite language.")

favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell'],
}

for key, value in favorite_languages.items():
	print(f"\n{key.title()}'s favorite languages are:")
	for language in value:
			print(f"\t{language.title()}")