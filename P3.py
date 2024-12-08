#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?
import math


def is_prime(num):
    a = math.sqrt(num)
    a = int(a) + 1
    for i in range(a):
        if i != 0 and i != 1:
            if num % i == 0:
                return False
    return True

def prime_factor(num):
    a = math.sqrt(num)
    a = int(a) + 1
    prime_factor_list = []
    for i in range(a):
        if i != 0 and is_prime(i) :
            if num % i == 0:
                prime_factor_list.append(i)
    
    return max(prime_factor_list)


print(prime_factor(600851475143))