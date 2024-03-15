"""lambda function examples"""

def myfunc(n):
    """ function that tripplles the numbder"""
    return lambda a : a * n

mynum = myfunc(2)
print(mynum(11))


#Example 2
def func(n):
    """function"""
    return lambda a : a * n


#func can be summarized as this
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


var = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formatting:", var(1000000))
print("float formatting:", var(999999.789541235))


even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in even_list:
    print(item())
