n = int(input())
string = input().split()

result = ""
for elem in string:
    result += elem

for i in range(len(result)):
    print(result[i], end="")
    if ((i+1) % 5 == 0):
        print()