import numpy as np
import pandas as pd

# a = np.random.randint(10, size=10)
# b = pd.Series(a)
# # print(b)
# # target = b[b % 3 == 0]
# # print(target)
# target = b.where(b % 3 == 0)
# target = target.dropna()
# print(target)
lst = ['Apple', 'Orange', 'Plan', 'Python', 'Money']
ser = pd.Series(lst)
vowels = list("aeiou")
list_v = []
# print(vowels)
for i in lst:
    temp = i.lower()
    count = 0
    for s in temp:
        if s in vowels:
            count += 1
    if count > 1:
        list_v.append(i)
new = pd.Series(list_v)
print(new)
