
cnt_arr = [0] * 4


for i in range(3):
    tf, temper = list(input().split())


    temper=int(temper)

    if tf=='Y' and temper >= 37:
        cnt_arr[0]+=1
        continue
    elif tf=='N' and temper >= 37:
        cnt_arr[1]+=1
        continue
    if tf=='Y' and temper < 37:
        cnt_arr[2]+=1
        continue
    else:
        cnt_arr[3]+=1
        continue

if cnt_arr[0] >= 2:
    cnt_arr.append('E')

for i in range(len(cnt_arr)):
    print(cnt_arr[i], end=" ")
