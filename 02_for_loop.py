# for iteration in range():
#     pass

# for iteration in iterableItem():
#     pass

# for loop with range with single input
for i in range(5):
    print(i)

for i in range(0, 5):
    print(i)

for i in range(0, 5, 1):
    print(i)

for i in range(0, 5, 2):
    print(i)

##
my_list = [1, 3, 2, 5, 6, 5]
for i in range(len(my_list)):
    print(i, my_list[i])

i = 0
for each_item in my_list:
    print(i, each_item)
    i += 1

# loop using enumerate
for i, val in enumerate(my_list):
    print(i, val)

# for loop in dict
my_dict = {
    "Name": "Rohan",
    "Age": 35,
    "Gender":"Male"
}

# access keys
print(my_dict.keys())

# for loop values
for each_key in my_dict.keys():
    print(each_key, my_dict[each_key])

# access each items
for each_item in my_dict.items():
    print(each_item)