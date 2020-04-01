def is_prime(num) :
    for i in range(2,num) :
        if num % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(6))
print(is_prime(97))
print(is_prime(105))
print(is_prime(997))
print(is_prime(999))