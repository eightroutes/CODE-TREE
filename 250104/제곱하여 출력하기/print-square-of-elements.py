n = int(input())

arr = list(map(int, input().split()))

arr_s = [elem**2 for elem in arr]

for elem in arr_s:
    print(elem, end=" ")