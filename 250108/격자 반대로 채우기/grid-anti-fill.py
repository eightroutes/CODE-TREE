n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if((i+1) % 2 == n % 2):
            arr[j][i] = cnt
        else:
            arr[n-j-1][i] = cnt
        cnt+=1


for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()