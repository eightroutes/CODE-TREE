arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

res1 = 0
res2 = 0
res3 = 0

for i in range(2):
    for j in range(4):
        res1 += arr[i][j]
    print(round(res1/4,1), end=" ")
    res1 = 0
print()

for j in range(4):
    for i in range(2):
        res2 += arr[i][j]
    print(round(res2/2,1), end=" ")
print()

res3 = (sum(arr[0]) + sum(arr[1])) / 8
print(round(res3,1))

