input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Write your code here!

for i in range(len(queries)):
    if queries[i] == 1:
        input_str = input_str[1:]+input_str[0]
        print(input_str)
    elif queries[i] == 2:
        input_str = input_str[-1]+input_str[0:-1]
        print(input_str)
    elif queries[i] == 3:
        input_str = input_str[::-1]
        print(input_str)