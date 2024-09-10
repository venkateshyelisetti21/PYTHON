def getDiscount(bill):
    if bill < 500 : return 5
    elif bill >= 500 and bill < 2500: return 10
    else: return 20
bill = int(input())
print(str(getDiscount(bill)) + "%")
