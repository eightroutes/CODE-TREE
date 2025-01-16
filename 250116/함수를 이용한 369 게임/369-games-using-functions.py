a, b = map(int, input().split())

# Write your code here!

def is_third(n):
    if n % 3 == 0:
        return True
    while n > 0:
        if n % 10 in [3, 6, 9]:
            return True
        n //= 10

def count_third(a, b):
    sum_v = 0
    for i in range(a, b+1):
        if is_third(i):
            sum_v += 1
    return sum_v


print(count_third(a,b))
    
