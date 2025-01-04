arr = list(map(int, input().split()))


for elem in arr:
    if elem == 0:
        zeroIdx = arr.index(elem)
        break

sum = arr[zeroIdx-1]+arr[zeroIdx-2]+arr[zeroIdx-3]

print(sum)