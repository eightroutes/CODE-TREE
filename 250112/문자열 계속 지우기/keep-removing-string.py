A = input()
B = input()

# Write your code here!



while True:
    if B in A:
        idx = A.index(B)
        A = A[0:idx] + A[idx+len(B):]
    else:
        break

print(A)
