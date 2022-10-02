# Q3.1
a = ('a', 1)
b = ('b', 2)
d = {}
d[a[0]] = a[1]
d[b[0]] = b[1]
# output is "{'a': 1, 'b': 2}"

# Q3.2

a = ('a', 1)
b = ('b', 2)
c = [a, b]
d = dict(c)

# output is "{'a': 1, 'b': 2}"
