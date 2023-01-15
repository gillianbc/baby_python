
# An immutable list is a tuple - we use ordinary brackets, not square ones to define the tuple
# but we still use square brackets to access the element at a particular index position

dimensions = (40, 10, 20)
print(dimensions[0])
print(dimensions[2])

# To define a tuple with a single element (bit useless really), you still need a comma
singular_tuple = (23,)
print(singular_tuple[0])

# Looping through a tuple
for dimension in dimensions:
    print(f'Element is {dimension}')

# Redefining a tuple
dimensions = (10, 1, 32)
for dimension in dimensions:
    print(f'Element is {dimension}')
