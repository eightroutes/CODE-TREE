n, m = map(int, input().split())

# Write your code here!
def gcd(n,m):
    result = 0
    div = min(n,m)
    for i in range(1, div+1):
        if n % i == 0 and m % i == 0:
            result = i
    return(result)

print(gcd(n,m))


