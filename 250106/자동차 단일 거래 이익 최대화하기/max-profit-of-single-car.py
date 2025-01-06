n = int(input())
price = list(map(int, input().split()))

result = []
isNotZ =False
for i in range(n):
    min_v = price[i]
    max_v = 1
    for j in range(i+1, n):
        if price[j] - min_v > max_v:
            max_v = price[j] - min_v
            isNotZ = True
        result.append(max_v)

if isNotZ == False:
    print(0)
else: 
    print(max(result))






