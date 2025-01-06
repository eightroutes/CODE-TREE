n = int(input())
price = list(map(int, input().split()))

# Write your code here!

min_p = min(price)
idx = price.index(min_p)
max_p = 0
for i in range(idx, n):
    if price[i] > max_p:
        max_p = price[i]

print(max_p-min_p)

