'''
Lec 6
'''

for letter in ['a','b','c']:
    print (letter)
    
demo_string = 'this is my string'

for c in demo_string:
    print(c)

for word in demo_string.split():
    print(word)

for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

for i in range(1,5,2):
    print(i)

'''
breakpoint is a function of IDE used for debugging
'''

#algorithms

num_list = [213, 321, 123, 312]
max_num = num_list[0]

for num in num_list:
    if max_num <= num:
        max_num = num

print(max_num)