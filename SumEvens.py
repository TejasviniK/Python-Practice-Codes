def sum_evens(minimum, maximum):
    sum = 0
    for i in range(minimum, maximum+1) :
        if i%2 == 0 :
            sum += i
    return sum
print(sum_evens(2, 6))
print(sum_evens(-2, 2))
print(sum_evens(5, 17))
