arr = list(map(int, input().split()))

cnt_arr = [0]*10

for elem in arr:
    if elem == 0:
        break
    cnt_arr[elem//10] += 1

for i in range(1,10):
    print(f"{i} - {cnt_arr[i]}")
