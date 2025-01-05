tf, temper = list(input().split())

cnt_arr = [0] * 4

temper=int(temper)

if tf=='Y' and temper >= 37:
    cnt_arr[0]+=1
elif tf=='N' and temper >= 37:
    cnt_arr[1]+=1
if tf=='Y' and temper < 37:
    cnt_arr[2]+=1
else:
    cnt_arr[3]+=1

if cnt_arr[0] >= 2:
    cnt_arr.append('E')

for i in range(len(cnt_arr)):
    print(cnt_arr[i], end=" ")
