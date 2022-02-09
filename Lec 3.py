'''
lec
'''

my_list = [1,2,3,4,5]
print(my_list)

my_nested_list = [1,2,3,my_list]
print(my_nested_list)

my_list[0] = 6
print(my_list)

print(my_list[0])
print(my_list[-1])
print(my_list[1])

print(my_list[1:3])
print(my_list[:3])
print(my_list[1:])
print(my_list[:])

x,y = ['a','b']

print(x)
print(y)

my_list.append(7)
print(my_list)
#add thing to list

my_list.remove(7)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list + [8,9])

my_list.extend(['a','b'])
print(my_list)

print('a' in my_list)
#to find out if a thing is in the list

print('c' in my_list)

print(len(my_list))
#length of the list

my_letters = ['a','b','b','c']
print(set(my_letters))

my_unique_letters = set(my_letters)
print(my_unique_letters)

