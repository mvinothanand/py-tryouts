# Find the largest prime factor of the given number
# example:  for 13195, 29 is the largest prime factor
from math import sqrt

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    
    if n < 2:
        return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False

    return True            


def get_next_prime(n: int) -> int:
    if n < 2:
        return 2
    else:
        while (True):
            if is_prime(n + 1):
                return n + 1
            n += 1

def main():
    #print(is_prime(int(input('n: '))))
    #print(get_next_prime(int(input('n: '))))
    n = int(input('n: '))
    # Method 1
    # Not efficient for larger numbers
    # largest_prime_factor = 2
    # if is_prime(n):
    #     largest_prime_factor = n
    # else:
    #     factor = 2
    #     boundary = n/2 + 1
    #     lowest_prime_factor = None
    #     while (factor < boundary):
    #         if n % factor == 0:
    #             if not lowest_prime_factor:
    #                 lowest_prime_factor = factor
    #                 boundary = n // lowest_prime_factor + 1
    #             largest_prime_factor = factor
    #         factor = get_next_prime(factor)

    #Method 2
    largest_prime_factor = -1
    factor = 2
    while ( factor * factor <= n):
        print(f'factor is now {factor}')
        while(n % factor == 0):
            largest_prime_factor = factor
            n = n // factor
            print(f'n is now {n}')
        factor += 1
    if n > 1:
        largest_prime_factor = n

    print(largest_prime_factor)



if __name__ == '__main__':
    main()