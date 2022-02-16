#3.1
str_list = ['a','d','e','b','c']
str_list.sort()
print(str_list)

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
print(str_list[2])

#3.5
#my_list = ['a',123,'123','b','B','false',false,123,None,'None']
#print(len(my_list))

#print( len(set(my_list)))

#3.6 find amount of words in string
og_str = 'this is my third python lab'
new_str = og_str.split()
print(len(new_str))

#3.7 sort numbers w/o min or max functions
num_list = [12,32,43,35]
num_list.sort()
print(num_list[0])
print(num_list[-1])

#3.8 edit nested list
game_board = [[0,0,0],[0,0,0],[0,0,0]]
game_board[1][1] = [1]
print(game_board)