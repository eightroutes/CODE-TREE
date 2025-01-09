st = list(input().split())

if len(st[0]) > len(st[1]):
    print(st[0], len(st[0]))
elif len(st[1]) > len(st[0]):
    print(st[1], len(st[1]))
else:
    print("same")