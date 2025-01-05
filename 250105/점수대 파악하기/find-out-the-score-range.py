arr = list(map(int, input().split()))

grade_arr = [0] * 10

for elem in arr:
    if elem == 0:
        break
    idx = 10 - (elem // 10)
    grade_arr[idx] += 1   

for i in range(10):
    print(f"{100-10*i} - {grade_arr[i]}")