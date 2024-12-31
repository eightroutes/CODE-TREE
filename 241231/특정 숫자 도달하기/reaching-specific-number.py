arr = list(map(int, input().split()))

sum = 0
index = 0

for i in range(10):
    if(arr[i] >= 250):
        break
    sum+=arr[i]
    index = i

print(sum, sum/i)
