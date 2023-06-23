#recursion
def addNumber(N):
    if N == 1:
        return 1
    else:
        return N + addNumber(N-1)

print(addNumber(100))
