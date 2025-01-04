arr = list(map(int, input().split()))

grade_arr = [100-10*i for i in range(10)]

print(grade_arr)

for elem in arr:
    if elem == 0:
        break
    idx = grade_arr.index(elem//10*10) 
    grade_arr[idx] += 1

for i in range(10):
    print(f"{(100-10*i) - grade_arr[i]}")
    
