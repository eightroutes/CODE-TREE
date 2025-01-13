a = input()
b = input()

str_a = ""
str_b = ""

for i in range(len(a)):
    if a[i].isdigit():
        str_a += a[i]

for i in range(len(b)):
    if b[i].isdigit():
        str_b += b[i]

a = int(str_a)
b = int(str_b)
print(a+b)