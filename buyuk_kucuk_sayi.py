list1 = [12,45,12,24,1000,345,500,365,500,1002,5]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]
    else:
        if secondmax == mx:
            secondmax = list1[i]

mn = min(list1[0], list1[1])
secondmn = max(list1[0], list1[1])
for i in range(2, n):
    if list1[i] < mn:
        secondmn = mn
        mn = list1[i]
    elif list1[i] < secondmn and mn != list1[i]:
        secondmn = list1[i]
    else:
        if secondmn == mn:
            secondmn = list1[i]

print("1. Büyük Sayı : ", str(mx))
print("2. Büyük Sayı : ", str(secondmax))
print("1. Küçük Sayı : ", str(mn))
print("2. Küçük Sayı : ", str(secondmn))
