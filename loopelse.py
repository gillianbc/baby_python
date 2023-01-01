for n in range(2, 10):
    is_prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            is_prime = False
            break
    # else:
    # loop fell through without finding a factor
    if is_prime:
        print(n, 'is a prime number')
