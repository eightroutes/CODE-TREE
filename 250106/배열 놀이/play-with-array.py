n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    quest = list(map(int, input().split()))

    if quest[0] == 1:
        print(arr[quest[1]-1])

    elif quest[0] == 2:
        arr_sec = []
        for elem in arr:
            if elem == quest[1]:
                arr_sec.append(arr.index(elem))
        if len(arr_sec) > 0:
            print(min(arr_sec)+1)
        else:
            print(0)
        
    elif quest[0] == 3:
        for i in range(quest[1]-1, quest[2]):
            print(arr[i], end=" ")
        print("")
