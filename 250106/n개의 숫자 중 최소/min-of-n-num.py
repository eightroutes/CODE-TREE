n = int(input())
a = list(map(int, input().split()))

# Write your code here!
min_val = a[0]
for elem in a:
    if elem < min_val:
        min_val = elem

print(min_val, a.count(min_val))