arr = list(map(int, input().split()))

max1 = 1
min1 = 1000
for elem in arr:
    if elem < 500 and elem > max1:
        max1 = elem
    elif elem > 500 and elem < min1:
        min1 = elem

print(max1, min1)
        