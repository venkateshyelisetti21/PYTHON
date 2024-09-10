def check(str):
    if len(str) >= 6 or str[0].isnumeric():return "Valid String"
    else:return "Invalid String"
str = input()
print(check(str))
