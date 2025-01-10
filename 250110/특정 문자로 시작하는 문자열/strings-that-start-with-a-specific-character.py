n = int(input())

arr = [
    input()
    for _ in range(n)
]

c = input()
cnt = 0
sum_v = 0

for elem in arr:
    if elem[0] == c:
        cnt += 1
        sum_v += len(elem)

print(cnt,f"{sum_v/cnt:.2f}")
