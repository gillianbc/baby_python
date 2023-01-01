# Numbers that have both 2 and 5 as factors
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# Numbers that are not divisible by 2 and divisible by 5
num_list2 = [y for y in range(100) if y % 2 != 0 if y % 5 == 0]
print(num_list2)

# This does not work - the OR is treated as an AND, even with the brackets
# i.e. it's numbers that are divisible by 7 AND 3
num_list2 = [y for y in range(100) if ( y % 7 == 0 | y % 3 == 0)]
print(num_list2)

# The above is the same as this:
num_list2 = [y for y in range(100) if y % 7 == 0 if y % 3 == 0]
print(num_list2)