string = input()

string = list(string)

string.pop(1)
string.pop(-2)

print("".join(string))