def fib_sum(lim):
    fib1 = 1
    fib2 = 2
    even = 2
    while even < lim:
        fib1 = fib1 + fib2
        if fib1 % 2 == 0:
            even += fib1
        fib2 = fib1 + fib2
        if fib2 % 2 == 0:
            even += fib2
    return even
print(fib_sum(4000000))
