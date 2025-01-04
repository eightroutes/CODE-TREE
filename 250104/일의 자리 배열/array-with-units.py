a, b = map(int, input().split())

arr = [a, b]

for i in range(2,10):
    arr.append((arr[i-2]+arr[i-1])%10)

for i in range(10):
    print(arr[i], end=" ")




    