'''
tuple: is immutable once created (cannot append)
'''

#my_tuple = 'a','b','c','d','e'
#print(my_tuple)

#my_second_tuple = ('a','b','c','d','e')
#print(my_second_tuple)

#not_a_tuple = ('a')
#print( type(not_a_tuple)   )

#a_tuple = ('a',)
#print( type( a_tuple)  )

#print(my_tuple[1])

#print(my_second_tuple[1:3])

'''
Dictionary is a collection of key value pairs

with JSON files, treat as dictionary
'''

my_car = {
    'color':'red',
    'maker': 'toyota',
    'year':2015
    }

print(my_car.get('color'))
#or
print(my_car['maker'])

print(my_car.items())
print(my_car.values())
print(my_car.keys())

#adding new entry in dictionary
my_car['model']='corola'

print(my_car['model'])

print('year' in my_car)