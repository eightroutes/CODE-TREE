arr = list(map(int, input().split()))

max_idx = arr[0]

for elem in arr:
    if elem > max_idx:
        max_idx = elem

print(max_idx)