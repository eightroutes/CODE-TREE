n = int(input())

arr = list(map(int, input().split()))

rev_arr = arr[::-1]

for elem in rev_arr:
    if elem % 2 == 0:
        print(elem, end=" ")
