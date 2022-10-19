# import random
#
# customers = ["Alex", "Bob,", "Carol", "Dave", "Flow", "Katie", "Nate"]
# # discount = {x: random.randint(1, 100) for x in customers}
# discount = {}
# for customer in customers:
#     discount[customer] = random.randint(1, 100)
# print(discount)
# new_discount = {}
# for item in discount.items():
#     if item[1] < 35:
#         new_discount[item[0]] = item[1]
# print(new_discount)


# mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# mySet = set()
# for i in range(1, 11):
#     mySet.add(i)
# print(mySet)
# def my(n):
#     if n%2==0:
#         return n
#     else:
#         return 0
# newSet=list(map(my,mySet))
# print(newSet)


# lst1 = [i for i in range(0, 10, 2)]
# lst2 = [i ** 2 for i in lst1]
# dic1 = dict(zip(lst1, lst2))
# print(dic1)
#
# dic2 = {}
# for i in range(0, 10, 2):
#     dic2[i] = i ** 2
# print(dic2)
#
# dic3 = {k: k ** 2 for k in range(0, 10, 2)}
# print(dic3)

# lst = [1, 34, 23, 56, 89, 44, 92]
# lst1 = list(filter(lambda x: (x % 2 != 0), lst))
# print(lst1)
#
#
# def my(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
# lst2 = list(filter(my,lst))
# print(lst2)
#
# def myfunc(x):
#     if x % 2 == 0:
#         pass
#     else:
#         return x
#
#
# lst2 = list(map(myfunc, lst))
# print(lst2)


# fahs = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
# # cel = [round((x - 32) * 5 / 9) for x in fahs.values()]
# cel = list(map(lambda x: round((x - 32) * 5 / 9), fahs.values()))
# print(cel)
# cels = dict(zip(fahs.keys(), cel))
# print(cels)

# names = ['Yuqi Lan', 'Marilyn Leung', 'Chenyu Zhang', 'WiingSze Wong']
# first = set()
# for i in names:
#     temp = i.split()
#     first.add(temp[0])
# print(first)
#
# last = set(list(i.split()[-1] for i in names))
# print(last)
#
# lasts = sorted(names, key=lambda x: x.split()[-1])
# print(lasts)

# def lastname(x):
#     return x.split()[-1]
#
#
# last_new = sorted(names, key=lastname)
# print(last_new)
#
# infile = open("States.txt", 'r')
# states = [x.rstrip() for x in infile]
# print(states)
# states = states[:14]
# states.sort()
# print(states)
#
# for i in range(12):
#     print(states[i] + ',' + ' ', end='')
# print(states[13])

def isPalindrome(astr, start, end):
    if start == end or start > end:
        return True
    elif astr[start] == astr[end]:
        return isPalindrome(astr, start + 1, end - 1)
    return False


read = input("input your word: ")
print(isPalindrome(read, 0, len(read) - 1))
