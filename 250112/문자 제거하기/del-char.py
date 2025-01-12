s = input()
s = list(s)

while len(s) > 0:
    if len(s) == 1:
        break

    n = int(input())

    if n >= len(s):
        s.pop()
        print(''.join(s))
    else:
        s.pop(n)
        print(''.join(s))


