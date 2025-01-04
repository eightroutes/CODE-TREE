arr = list(map(int, input().split()))

for elem in arr:
    if elem % 3 == 0:
        k = arr.index(elem)
        break

print(arr[k-1])
