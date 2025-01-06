n1, n2 = map(int, input().split())
n1_arr = list(map(int, input().split()))
n2_arr = list(map(int, input().split()))

result = []
idx = 0
found = False
for i in range(n1):
    for j in range(n2):
        if n1_arr[i] == n2_arr[j]:
            idx = i
            found = True
            break
    if found:
        break
            
for k in range(idx, idx+len(n2_arr)):
    result.append(n1_arr[k])

# print(result)
if(result == n2_arr):
    print("Yes")
else: 
    print("No") 