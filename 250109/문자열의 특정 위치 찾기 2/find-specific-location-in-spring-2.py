arr = ['apple','banana','grape','blueberry','orange']
c = input()

cnt = 0
for row in arr:
    if c == row[2] or c == row[3]:
        print(row)
        cnt+= 1

print(cnt)