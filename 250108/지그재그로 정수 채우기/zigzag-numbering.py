n, m = map(int, input().split())

# Write your code here!
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

x = 0

for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            arr[i][j] = x
        else:
            arr[n-i-1][j] = x
        x+=1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()