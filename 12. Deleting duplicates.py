def my_func(x):
    return tuple(dict.fromkeys(x))
print(my_func([1,2,2,3,4,4]))