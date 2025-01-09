n, m = list(map(int, input().split()))

arr = [
    [ 0 for _ in range(n+1)]
    for _ in range(n+1)
]

for _ in range(m):
    r, s = tuple(map(int, input().split()))
    arr[r][s] = r*s

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end = " ")
    print()



