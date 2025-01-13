arr = []
while True:
    s = input()
    if s == '0':
        break
    arr.append(s)

cnt = len(arr)
print(cnt)
for i in range(0, cnt, 2):
    print(arr[i])



