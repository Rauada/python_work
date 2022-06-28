# Asks the user how many people are in the dinner group.
people = input("How many people will be dining with you tonight, kind sir?")

# Change people input string to integer
people = int(people)

# If the answer is more than eight, print a message saying they will have to wait for a table.
# Otherwise, report that their table is ready.
if people > 8:
	print("You're table is not ready, please wait a moment while we prepare it.")
else:
	print("You're table is ready, please come with me.")	