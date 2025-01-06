n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(n):
    a = arr[i]
    for j in range(i+1, n):
        b = arr[j]
        result.append(b-a)

print(min(result))
