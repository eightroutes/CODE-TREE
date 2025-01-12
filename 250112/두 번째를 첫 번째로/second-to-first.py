s = list(input())

s1 = s[0]
s2 = s[1]

for i in range(len(s)):
    if s[i] == s2:
        s[i] = s1

print("".join(s))


