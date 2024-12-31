arr = list(map(int, input().split()))

sum = 0

for i in range(10):
    if(arr[i] >= 250):
        break
    sum+=arr[i]
    index = i+1

average = round(sum/index, 1)

print(sum, average)
