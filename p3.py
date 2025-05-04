def prime(num):
    itr = int((num)**(1/2)) + 1
    for i in range(2, itr):
        if num % i == 0:
            return False
    return True

def factors(num):
    fact = []
    itr = int((num)**(1/2)) + 1
    print(itr)
    for i in range(2, itr):
        if prime(i):
            if num % i == 0:
                fact.append(i)
                
    return fact[-1]

print(factors(600851475143))