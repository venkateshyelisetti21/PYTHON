def evenOrOdd(num):
    for i in range(num + 1):
        if i % 2: print(str(i) + " ODD")
        else: print(str(i) + " EVEN")
num = int(input())
evenOrOdd(num)
