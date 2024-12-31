arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

sum_val = 0

for elem in arr[:cnt]:
    sum_val+=elem

avg = sum_val / (cnt)

print(sum_val, f"{avg:.1f}")
