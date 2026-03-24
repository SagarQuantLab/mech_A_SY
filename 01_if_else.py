# if else

# if block
my_age = 18
if my_age > 18:
    print("Adult")

# if else block
if my_age > 18:
    print("Adult")
else:
    print("Minor")

# if elif else block
if my_age > 18:
    print("Adult")
elif my_age == 18:
    print("Turing Adult")
else:
    print("Minor")


# reduce code
my_age = 18
msg = "Bye"
if isinstance(my_age, int):
    msg = "hello"
print(msg)