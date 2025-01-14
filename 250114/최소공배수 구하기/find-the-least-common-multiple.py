n, m = map(int, input().split())

# Write your code here!
def lcm(n, m):
    div = min(n,m)
    result = 0
   
    for i in range(div, 0, -1):
        if n % i == 0 and m % i == 0:
            result = i*(n//i)*(m//i)
            break

    return result

print(lcm(n,m))