a = int(input())
cnt = 0

arr=[a]

i=0
while True:
    if (arr[i] % 5) == 0:
        cnt+=1
    if(cnt == 2):
        break
    arr.append(arr[i]+a)
    i+=1
    
for elem in arr:
    print(elem, end=" ")