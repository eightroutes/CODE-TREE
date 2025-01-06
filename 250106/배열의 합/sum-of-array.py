n = 4

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

for elem in arr:
    print(sum(elem))