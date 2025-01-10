n = int(input())

arr = [
    input()
    for _ in range(n)
]

string = ""

for elem in arr:
    string+=elem

print(string)