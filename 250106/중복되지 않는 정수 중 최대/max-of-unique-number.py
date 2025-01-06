n = int(input())
nums = list(map(int, input().split()))


# Write your code here!
max_num = 0
cntp = 0
for elem in nums:
    if nums.count(elem) == 1:
        cntp+=1
        if max_num < elem:
            max_num = elem

if cntp == 0:
    print(-1)
else:
    print(max_num)
    
    

