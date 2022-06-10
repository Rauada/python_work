# for value in range(1,6):
# 	print(value)

# passing one argument to range makes it start from zero
# for value in range(6):
# 	print(value)

# numbers = list(range(1,11))
# print(numbers)

# for number in numbers:
# 	print(f"The number is {number}")

# listing even numbers from 1 to 10
# even_numbers = list(range(2,11,2))
# print(even_numbers)

# make a list of the first 10 square numbers
# squares = []
# for value in range(1,11):
# 	squares.append(value**2)
# print(squares)

# print(f"Minimum value: {min(squares)}")
# print(f"Maximum value: {max(squares)}")
# print(f"Sum of values: {sum(squares)}")

# list comprehension
# squares = [value**2 for value in range(1,11)]
# print(squares)

# values = range(1,21)
# for value in values:
# 	print(value)

# values = range(1,1_000_001)
# print(min(values))
# print(max(values))
# print(sum(values))


# odd_numbers = range(1,21,2)
# for number in odd_numbers:
# 	print(number)


# numbers = range(3,31,3)
# for number in numbers:
# 	print(number)

cubed = [value**3 for value in range(1,11)]
for number in cubed:
	print(number)