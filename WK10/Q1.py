import numpy as np
import random

lst = []
for i in range(11):
    lst.append(i)
print(lst)
ts = np.array(lst)
print(ts)
ts = np.where(ts % 2 == 1, -1, ts)
print(ts)

# %%
arr1 = np.random.randint(10, size=(9))
arr1 = arr1.reshape(3, 3)
print(arr1)

# %%
arr2 = np.random.randint(10, size=(9))
arr2 += 202
print(arr2)

# %%
arr3 = np.random.randint(30, 41, size=(10))
print(arr3)

# %%
arr4 = np.random.randint(10, size=(10))
arr5 = np.random.randint(10, size=(10))
print(arr4)
print(arr5)
print(np.where(arr4 > arr5))
print(np.where(arr4 == arr5))

# %%
arr6 = np.random.randint(10, size=(10, 10))
arr7 = arr6[..., : 4]
print(arr6)
print(arr7)
print(arr7.reshape(5, -1))
