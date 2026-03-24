# STRING SLICING

my_string = "This is Mech students"

# first letter
print(my_string[0])

# second letter
print(my_string[1])

# access 'This'
print(my_string[0:4])

# access 'Ti'
print(my_string[0:4:2])

# access the last letter
print(my_string[-1])

# second last letter
print(my_string[-2])

# reverse string
print(my_string[::-1])

# reverse students
print(my_string[:-9:-1])

# upper /lower case
print(my_string.upper())
print(my_string.lower())

# replace
print(my_string.replace('s', 'X'))