n = int(input())
arr = list(map(int, input().split()))

cnt = 0
idx = 0
for i in range(len(arr)):
    if arr[i] == 2:
        cnt += 1
    if cnt == 3:
        idx = i
        break

print(idx+1)