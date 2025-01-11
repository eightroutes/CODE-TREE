string = input()

arr = list(string)

arr[1] = 'a'
arr[-2] = 'a'

string = "".join(arr)

print(string)