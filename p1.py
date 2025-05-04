def sum_mul(num, div):
    mul = (num - 1) // div
    return div * mul * (mul + 1) // 2

lim = 1023570000
print(f"Sum of multiples of 3 or 5 below {lim} is {sum_mul(lim, 3) + sum_mul(lim, 5) - sum_mul(lim, 15)}.")