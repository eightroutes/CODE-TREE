n, m = list(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

x = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = x
        x+=1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()