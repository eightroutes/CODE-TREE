arr = list(map(int, input().split()))

sum_e = 0
sum_o = 0

for i in range(len(arr)):
    if i % 2 != 0:
        sum_o += arr[i]
    elif i % 2 == 0:
        sum_e += arr[i]

result = abs(sum_o - sum_e)

print(result)