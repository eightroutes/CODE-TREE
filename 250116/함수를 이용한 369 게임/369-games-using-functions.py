a, b = map(int, input().split())

# Write your code here!

def count_third(n):
    if n % 3 == 0:
        return True
    while n > 0:
        digit = n % 10
        if digit in (3, 6, 9):
            return True
        n //= 10
    return False

def from_to(a, b):
    sum_v = 0
    for i in range(a, b+1):
        if count_third(i):
            sum_v+=1
    return sum_v

print(from_to(a,b))

