a, b = input().split()

int_a = 0 
int_b = 0

for i in range(len(a)):
    if a[i].isdigit() == False:
        int_a = int(a[:i])
        break
for i in range(len(b)):
    if b[i].isdigit() == False:
        int_b = int(b[:i])
        break

print(int_a + int_b)