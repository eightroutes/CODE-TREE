arr = list(map(int, input().split()))

index = 10
if 0 in arr:
    index = arr.index(0)

for elem in arr[index-1::-1]:
    print(elem, end=" ")