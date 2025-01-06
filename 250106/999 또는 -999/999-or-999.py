arr = list(map(int, input().split()))

max_v = arr[0]
min_v = arr[0]
for elem in arr:
    if elem == 999 or elem == -999:
        break
    if elem > max_v:
        max_v = elem
    if elem < min_v:
        min_v = elem

print(max_v, min_v)