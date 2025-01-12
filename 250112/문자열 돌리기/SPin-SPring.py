string = input()

leng = len(string)

print(string)

for _ in range(leng):
    string = string[-1] + string[:-1]
    print(string)