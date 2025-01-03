arr = list(map(int, input().split()))
cnt_even = 0
sum_val = 0

for elem in arr:
    if elem == 0:
        break 
    if elem % 2 == 0:
        cnt_even += 1
        sum_val += elem

print(cnt_even, sum_val) 