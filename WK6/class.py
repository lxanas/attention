# def myfunc(a, b):
#     sum = a + b
#     sub = a / b
#     mul = a * b
#     return a, b
#
#
# c, d = myfunc(1, 2)
# print(c)

# def ex3(num):
#     namelist = [20, 30, 1, 22, 33, 44, 5]
#     if num in namelist:
#         return True
#     else:
#         return False

# def ex5(a, b, c):
#     return max(a, b, c)

def ex6(astr):
    vowel = ['a', 'e', 'i', 'o', 'u']
    temp = astr.lower()
    vowelnum = 0
    other = 0
    for s in temp:
        if s in vowel:
            vowelnum += 1
        elif s != ' ':
            other += 1
    return vowelnum, other


print(ex6("hEllo world"))
