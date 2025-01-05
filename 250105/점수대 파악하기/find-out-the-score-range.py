arr = list(map(int, input().split()))

count_arr = [0] * 11

for elem in arr:
    if elem == 0:
        break
    if elem < 10:
        continue
    count_arr[elem//10] += 1


for i in range(10, 0, -1):
    print(f"{i}0 - {count_arr[i]}")