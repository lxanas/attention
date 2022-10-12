astr = input("Enter a sentence: ").upper()
dic = {chr(x): 0 for x in range(65, 91)}
for i in astr:
    if 64 < ord(i) < 91:
        dic[i] += 1
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
for k, v in dic.items():
    if v > 0:
        print(k + ": " + str(v))
