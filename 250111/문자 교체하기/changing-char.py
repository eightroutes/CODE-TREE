a, b = input().split()

a = list(a)
b = list(b)

b[0] = a[0]
b[1] = a[1]

b = "".join(b)

print(b)