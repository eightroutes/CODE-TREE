n = int(input())

# Write your code here!
def isTheNumber(n):
    return n % 2 == 0 and ((n//10) + (n%10)) % 5 == 0

if isTheNumber(n):
    print("Yes")
else:
    print("No")