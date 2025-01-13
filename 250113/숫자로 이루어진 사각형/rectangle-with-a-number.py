n = int(input())

# Write your code here!

def Rect(n):
    l = 1
    for i in range(n):
        for k in range(n):
            print(l, end=" ")
            l += 1
            if l == 10:
                l = 1
        print()     

Rect(n)     
        코드 실행


제출 및 채점


닫기

