y = int(input())

# Write your code here!
def leap_year(y):
    if y % 4 == 0:
        if not (y % 100 == 0 and y % 400 != 0):
            return True

if leap_year(y):
    print("true")
else:
    print("false")
    