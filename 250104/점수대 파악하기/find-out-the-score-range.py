arr = list(map(int, input().split()))

grade_arr = [100-10*i for i in range(10)]
count_arr = [0]*10


for elem in arr:
    if elem == 0:
        break
    idx = grade_arr.index(elem//10*10) 
    count_arr[idx] += 1
    

for i in range(10):
    print(f"{grade_arr[i]} - {count_arr[i]}")
    
