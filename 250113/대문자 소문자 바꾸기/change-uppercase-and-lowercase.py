s = input()

s = list(s)

for i in range(len(s)):
    if 'A' <= s[i] and s[i] <= 'Z':
        s[i] = s[i].lower()
    elif 'a' <= s[i] and s[i] <= 'z':
        s[i] = s[i].upper()

print(''.join(s))