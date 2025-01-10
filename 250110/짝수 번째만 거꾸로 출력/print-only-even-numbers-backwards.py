string = input()

n_s = []

for i in range(1, len(string), 2):
    n_s.append(string[i])

n_s = n_s[::-1]

for elem in n_s:
    print(elem, end="")