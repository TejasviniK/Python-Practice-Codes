def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else :
        return n * factorial(n-1)
    
def numCombinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))


print(numCombinations(52, 2))
print(numCombinations(10, 5))
print(numCombinations(4, 4))