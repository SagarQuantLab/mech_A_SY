#LIST
# [], index, duplicates allowed, ordered, mutable

my_list = [1, 3, 2, 5, 6, 5]

# first element
print(my_list[0])

# second element
print(my_list[1])

# access first to third element
print(my_list[0:3])

# access first and third element
print(my_list[0:3:2])

# last element
print(my_list[-1])

# reverse list
my_list.reverse()
print(my_list)

# replace first index by 5000
my_list[0] = 5000
print(my_list)