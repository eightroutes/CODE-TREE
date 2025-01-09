s1 = input()
s2 = input()

res = []

for elem in s1+s2:
    if elem != " ":
        res.append(elem)

for elem in res:
    print(elem, end="")
