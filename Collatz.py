def collatz(num) :
    count = 0
    while not num == 1:
        if num % 2 == 1:
            num = num * 3 + 1
        else :
            num = num / 2
        count += 1
    return count
        


print(collatz(5))
print(collatz(15))
print(collatz(25))