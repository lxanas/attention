# from functools import reduce
#
# lst = [1, 3, 5, 6, 2]
# print(reduce(lambda x, y: x + y, lst))
# print(reduce(lambda x, y: x if x > y else y, lst))

def squareR(x):
    return pow(x, 0.5)


def squart(x):
    return pow(x, 2)


def cube(x):
    return pow(x, 3)


func = [squareR, squart, cube]


def apply_func(L, x):
    result = {}
    for f in L:
        result[f.__name__] = round(f(x), 2)
    return result


num = int(input())
data = apply_func(func, num)
print(data)
key_data = sorted(data.items(), key=lambda k: k[0])
print(key_data)
value_data = sorted(data.items(), key=lambda k: k[1])
print(value_data)

print(type(value_data[0]))
