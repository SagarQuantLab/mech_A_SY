#DICT
# {}, keys, duplicates not allowed, ordered, mutable


my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender":"Male",
    "Name":"Sohan"
}

# call 'Rohan'
print(my_dict['Name'])

# get all keys
print(my_dict.keys())

# get all values
print(my_dict.values())

# get both key value pair
print(my_dict.items())

# change value of age
my_dict["Age"] = 25
print(my_dict)

##########################################################################
# ITEM      SYMBOL      CALLING       ORDERED       DUPLICATE       MUTABLE
# LIST        []         Index          Y               Y               Y
# DICT        {}          Keys          Y               N               Y
# TUPLE       ()         Index          Y               Y               N
# SETS        {}         -              N               N               N