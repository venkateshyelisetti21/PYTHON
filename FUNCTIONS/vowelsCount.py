def vowelsCount(str):
    a = "aeiou"
    cnt = 0
    for i in str:
        i = i.lower()
        if i in a: cnt += 1
    print(cnt)
str = input()
vowelsCount(str)
