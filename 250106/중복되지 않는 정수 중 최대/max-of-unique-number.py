n = int(input())
nums = list(map(int, input().split()))


# Write your code here!
       

nums_set = set(nums)

if len(nums_set) == len(nums) // 2:
    print(-1)
else:
    print(max(nums))