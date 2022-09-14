flag = 0
while flag == 0:
    password = input("Enter a password:")
    for s in password:
        if ('0' <= s <= '9') or ('a' <= s <= 'z') or ('A' <= s <= 'Z'):
            flag = 1
        else:
            flag = 0
    if len(password) < 6:
        flag = 0
    if flag == 1:
        print("Password set successfully")
