#3.1

for I in range(6):
    
    if I !=6:
        print(I)

#3.2

result = 1
for I in range(1,6):
    
    result = result * I

print(result)

#3.3

result = 0
for I in range(1,6):
    
    result = result + I

print(result)

#3.4

result = 1

for k in range(3,9):
   
   result = result * k
    
print(result)

#3.5

result = 1

for k in range(1,8):
    
    result = result * k
    
result_2 = 1

for I in range(1,4):
    
    result_2 = result_2 * I

print(result/result_2)

#3.6

string = 'this is my 6th string'
total = 1

for i in range(len(string)):
    if(string[i] == ' ' or string == '\n' or string == '\t'):
        total = total + 1

print("Total Number of Words in this String = ", total)

#3.7

