class a:
    x=2
    print('this is class a')
class b(a):
    x=4
    print('this is class b')
class c(b):
    x=6
    print('this is class c')
class d(c,b,a):
    print('this is d class')
a=d()
print(a.x)
