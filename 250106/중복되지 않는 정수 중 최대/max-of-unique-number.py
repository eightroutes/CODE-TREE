n = int(input())
nums = list(map(int, input().split()))


# Write your code here!
max_num = nums[0]

for elem in nums:
   
    if max_num <= elem:
        if elem == max_num:
            max_num=-1
        else:
            max_num = elem


print(max_num)
    

