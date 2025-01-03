arr = list(map(int, input().split()))
sum_even = 0
sum_third = 0

n = len(arr)

# arr_even = arr[::2]
# sum_even = sum(arr_even)
for i in range(1,n,2):
    sum_even += arr[i]

for j in range(2,n,3):
    sum_third += arr[j]

sum_avg = sum_third / 3.0

print(sum_even, f"{sum_avg:.1f}")