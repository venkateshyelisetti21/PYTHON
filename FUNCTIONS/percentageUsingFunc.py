def percent(n):
    if n < 1000:return n * 5 / 100
    else: return n * 10 / 100
n = int(input())
print(percent(n))
