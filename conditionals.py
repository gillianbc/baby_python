door_is_locked = False

if door_is_locked:
    print("Mum, open the door!")
else:
    print("Let's go inside")

for letter in 'Hello'[::-1]:
    print(letter)
print('---')
mylist = [1, 'a', 'Hello']
for obj in mylist:
    print(obj)

mylist = [[1,2,3],[4,5,6]]
for obj in mylist:
    print(obj)
print(mylist[1][2])

i = 1
while i < 4:
    print(i)
    i = i + 1