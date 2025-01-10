arr = [
    input()
    for _ in range(10)
]

c = input()

isNotNone = False
for elem in arr:
    if elem[-1] == c:
        print(elem)
        isNotNone = True

if isNotNone != True:
    print("None")
        
   


    