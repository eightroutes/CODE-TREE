n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

sum_v = str(sum(arr))

print(sum_v[1:]+sum_v[0])
