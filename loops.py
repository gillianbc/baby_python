toppings = ['cheese', 'onion', 'jalapeno', 'liver']

for topping in toppings:
    msg = f'I like {topping}'
    print(msg)

# Start at 1 and stop at 5 - the 5 is not printed
for num in range(1, 5):
    print(f'Your number is {num}')

# Prints starting at 0 if only 1 arg
for num in range(5):
    print(f'My number is {num}')

# 3rd arg is the step size
# This is a great way of creating a list of numbers
even_numbers = range(0, 11, 2)
for num in even_numbers:
    print(f'Even number: {num} with square {num ** 2}')

print(f'The min is {min(even_numbers)} and the max is {max(even_numbers)}')

# Can also create a list of numbers using this one-liner which combines the function and the for loop
# This is known as a list comprehension
squares = [num**2 for num in range(1,11)]
print(squares)

many_numbers = range(1, 1_000_001)
print(max(many_numbers))
total = 0
for num in many_numbers:
    total = total + num
print(f'Total is {total}')

# ex 4-6
odd_numbers = range(1, 21,  2)
print(f'Odd numbers {odd_numbers}')
for num in odd_numbers:
    print(num)

for num in (range(3, 30, 3)):
    print(num)

# ex 4.8
cubes = []
for num in range(1,11):
    result = num**3
    cubes.append(result)
    print(result)
print(cubes)

# ex 4.9 List comprehension
cubes_comprehension = [num**3 for num in range(1,11)]
print(cubes_comprehension)

