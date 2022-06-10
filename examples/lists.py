bicycles = ['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[-1].title()}"

# changes the value of list element
bicycles[0] = "diamondback"

# append a new item to the end of the list
# bicycles.append("caloi")
# print(bicycles)

# add a new item to the list at the specified index
bicycles.insert(2, "caloi")

# remove an item from the list
# del bicycles[4]

# pop the last item and store it for use
# popped_bicycles = bicycles.pop()


# remove an item from the list by its value
too_expensive = "redline"
bicycles.remove(too_expensive)

# sort a list alphabetically
# bicycles.sort(reverse=True)


# sort temporarily
# print(bicycles)
# print(sorted(bicycles))
# print(bicycles)


print(len(bicycles))