fruits = ['apple', 'pear', 'banana', 'orange', 'cherry']
# Slice - index of 1st element, index of lst element (not inclusive), step size
print(f'The first three items in the list are {fruits[:3]}')
print(f'The items after the 1st one are {fruits[1:]}')

print(f'Three items in the middle are {fruits[1:4]}')

print(f'The last item in the list is {fruits[-1:]}')
print(f'The last three items in the list are {fruits[-3:]}')

print(f'All items in the list: {fruits[:]}')

newfruits = fruits[:]
print(f'Cloned list is {newfruits}')
newfruits.append('lime')
fruits.append('lemon')
print(f'All items in the clone list: {newfruits[:]}')
print(f'All items in the original list: {fruits[:]}')

for fruit in fruits:
    print(f'Fruit is {fruit}')
for fruit in fruits[2:]:
    print(f'Fruits in a slice of fruit is {fruit}')
