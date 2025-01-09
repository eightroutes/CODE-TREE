n, m = list(map(int, input().split()))

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
cnt =1
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r-1][c-1] = cnt
    cnt+=1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()

