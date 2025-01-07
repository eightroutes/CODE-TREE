arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

sum_v = 0

for i in range(4):
    for j in range(i+1):
        sum_v+=arr[i][j]

print(sum_v)
