def my_list(list):
    list.extend(list)
    return list
a=[1,2,3,4]
print(my_list(a))