A = input()

# Write your code here!
arr = []
cnt = 1
for i in range(1, len(A)):
    if A[i-1] == A[i]:
        cnt+=1
        if A[i] not in arr:
            arr.append(A[i-1])
    elif A[i-1] != A[i]:
        if(arr==None):
            arr.append(A[i-1])
        arr.append(str(cnt))
        cnt = 1
        arr.append(A[i])
arr.append(str(cnt))

result = "".join(arr)
print(len(result))

for elem in arr:
    print(elem, end="")


