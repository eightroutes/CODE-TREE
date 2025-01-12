string = input()

leng = len(string)

print(string)
for i in range(1, leng):
    print(string[-i:] + string[0:leng-i])
print(string)