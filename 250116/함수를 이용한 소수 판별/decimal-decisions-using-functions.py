a, b = map(int, input().split())

# Write your code here!
def find_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def a_to_b_sum(a,b):
    sum_v = 0
    for i in range(a, b+1):
        if find_prime(i):
            sum_v += i
    return sum_v

print(a_to_b_sum(a,b))
        
    