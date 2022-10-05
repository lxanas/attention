def isVowelWord(a):
    a = a.lower()
    flag = True
    vowel = ['a', 'e', 'i', 'o', 'u']
    for v in vowel:
        if v not in a:
            flag = False
    return flag


if __name__ == '__main__':
    aa = input("enter a word: ")
    if isVowelWord(aa):
        print(aa+" contains every vowel")
    else:
        print(aa+" does not contain every vowel")
