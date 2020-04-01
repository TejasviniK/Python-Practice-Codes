def num_factors(num):
    count = 0
    for i in range(2,num):
        if num % i == 0:
            count += 1
    return count


print(num_factors(5))
print(num_factors(6))
print(num_factors(97))
print(num_factors(105))
print(num_factors(999))