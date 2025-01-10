st = input()
n = int(input())

st_reverse = st[::-1]

if n > len(st):
    print(st_reverse)
else:
    for i in range(0, n):
        print(st_reverse[i],end="")

