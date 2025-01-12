string = input()

string = list(string)

for i in range(len(string)):
    if string[i] == 'e':
        string.pop(i)
        break

print(''.join(string)) 