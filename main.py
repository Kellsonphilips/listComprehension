

# List comprehension helps us in the manipulation of a created list and creating a new list as well

# How we would create a new list from a pre list the normal way using for loop
numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    add_1 = n + 1
    new_numbers.append(add_1)
print(new_numbers)

# with list comprehension
new_numbers = [n + 1 for n in numbers]
print(new_numbers)
