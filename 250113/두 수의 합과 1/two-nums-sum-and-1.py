a, b = map(int, input().split())

sum_v = str(a+b)

result = 0

for elem in sum_v:
    if elem == "1":
        result += 1

print(result)

