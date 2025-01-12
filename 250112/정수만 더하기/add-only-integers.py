A = input()

sum_v = 0

for elem in A:
    if elem.isdigit():
        sum_v += int(elem)

print(sum_v)
