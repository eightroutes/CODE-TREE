a, b = map(int, input().split())

# Write your code here!

def count_third(n):
    return n % 3 == 0 or n // 10 == (3 or 6 or 9) or n % 10 == (3 or 6 or 9)

def from_to(a, b):
    sum_v = 0
    for i in range(a, b+1):
        if count_third(i):
            sum_v+=1
    return sum_v

print(from_to(a,b))

