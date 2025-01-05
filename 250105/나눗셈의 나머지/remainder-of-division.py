a, b = map(int, input().split())

rm_arr = [0]*10

while a > 1:
    rm = a % b
    rm_arr[rm] += 1
    a = a//b

res = [elem*elem for elem in rm_arr]

print(sum(res))