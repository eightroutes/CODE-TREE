n = int(input())

# Write your code here!
def sum_n(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v // 10

print(sum_n(n))
