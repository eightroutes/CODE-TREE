s, q = input().split()
q = int(q)

question = [
    list(input().split())
    for _ in range(q)
]

s = list(s)

for elem in question:
    if elem[0] == "1":
        a = int(elem[1])
        b = int(elem[2])
        s[a-1], s[b-1] = s[b-1], s[a-1]
        print("".join(s))

    elif elem[0] == "2":
        a = elem[1]
        b = elem[2]
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        print("".join(s))


    


