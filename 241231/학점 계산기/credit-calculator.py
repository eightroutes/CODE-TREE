n = int(input())

arr = list(map(float, input().split()))

sum_val = sum(arr)
avg_grade = sum_val/n

print(f"{avg_grade:.1f}")

if avg_grade >= 4.0:
    print("Perfect")
elif avg_grade >= 3.0:
    print("Good")
else:
    print("Poor")