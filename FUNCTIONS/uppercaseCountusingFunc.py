def uppercaseCharCount(str):
    cnt = 0
    for i in str:
        if i.isupper():cnt += 1
    print(cnt)
str = input()
uppercaseCharCount(str)
