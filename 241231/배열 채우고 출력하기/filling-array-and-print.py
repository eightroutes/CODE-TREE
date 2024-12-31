arr = list(input().split())

rev_arr = arr[::-1]

result = ""

for a in rev_arr:
    result+=a

print(result)
