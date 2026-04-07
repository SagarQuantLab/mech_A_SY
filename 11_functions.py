# def my_function(*args, **kwargs):
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise ValueError("First position input argument should be integer")
        if not isinstance(args[1], int):
            raise ValueError("Second position input argument should be integer")
        
        if len(kwargs) > 0:
            key_list = list(kwargs.keys())
            if not isinstance(kwargs[key_list[0]], int):
                raise ValueError("First option argument should be integer")
            if not isinstance(kwargs[key_list[1]], int):
                raise ValueError("Second option argument should be integer")
        else:
            kwargs.setdefault("c", 0)
            kwargs.setdefault("d", 0)
        
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def addition(a, b, c, d):
    sum = a + b + c + d
    return sum

print(addition(2, 3))
# print(addition(2, 3, 4))
# print(addition(2, 3, 4, 5))
print(addition(2, 3, c=4, d=5))
# print(addition(2, 3, c='c', d=5))
# print(addition('a', 3))