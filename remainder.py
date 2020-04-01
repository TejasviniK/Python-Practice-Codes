def remainder(divident, divisor):
    while(divident >= divisor):
        divident = divident - divisor
    return divident


print(remainder(9, 3))
print(remainder(11, 4))
print(remainder(27, 5))
