A = input()
B = input()

cnt = 0
for i in range(len(A)):
    A = A[-1] + A[0:-1]
    if A == B:
        cnt = i+1

if cnt == 0:
    print(-1)
else: 
    print(cnt)