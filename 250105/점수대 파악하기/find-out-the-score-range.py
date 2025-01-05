arr = list(map(int, input().split()))

cnt_arr = [0]*10

for elem in arr:
    if elem == 0:
        break
    if elem < 10:
        continue
    idx = 10 - (elem // 10)
    cnt_arr[idx] += 1

for i in range(10):
    print(f"{10-i}0 - {cnt_arr[i]}")
    
    