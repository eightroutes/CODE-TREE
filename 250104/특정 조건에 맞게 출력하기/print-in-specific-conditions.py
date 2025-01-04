arr = list(map(int, input().split()))

result = []

for elem in arr:
    if elem == 0:
        break

    if elem % 2 != 0:
        result.append(elem+3)
    else:
        result.append(elem//2)

for elem in result:
    print(elem, end=" ")
    
    