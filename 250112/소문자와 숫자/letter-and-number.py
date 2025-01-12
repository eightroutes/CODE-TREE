s = input()

for elem in s:
    if elem.isalpha():
        print(elem.lower(), end="")
    elif elem.isdigit():
        print(elem, end="")

        
