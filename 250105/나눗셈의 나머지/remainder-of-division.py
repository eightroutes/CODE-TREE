a, b = map(int, input().split())

rm_arr = [0]*9

while a > 1:
    a = a // b
    rm = a % b
    rm_arr[rm] += 1

res = [elem*elem for elem in rm_arr]

print(sum(res))