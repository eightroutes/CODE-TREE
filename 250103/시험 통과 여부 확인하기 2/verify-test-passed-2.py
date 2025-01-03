num = int(input())
cnt = 0

for i in range(num):
    sum_val = 0
    score = list(map(int, input().split()))
    for elem in score:
        sum_val += elem
    avg = sum_val / 4
    if (avg >= 60):
        print("pass")
        cnt+=1
    else:
        print("fail")

print(cnt)

