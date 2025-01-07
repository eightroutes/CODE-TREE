n, m = list(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(4)
]

x = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = x
        x+=1

for elem in arr:
    for elem_in in elem:
        print(elem_in, end=" ")
    print()