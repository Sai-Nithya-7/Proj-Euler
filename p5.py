def prime(num):
    itr = int((num)**(1/2)) + 1
    for i in range(2, itr):
        if num % i == 0:
            return False
    return True

def highest(prm, lim):
    while (prm < lim):
        prm *= prm
    return prm

def lcm(lim):
    num = 1
    for i in range(2, lim):
        if prime(i):
            num *= 

print(primes())