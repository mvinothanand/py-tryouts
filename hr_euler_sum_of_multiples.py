#https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true

def sum_of_multiples(max_value, factor):
    # Using the summation formula of arithmetic progression is best
    # Formula: 
    # n - number of terms, d - common difference, a1 - first term
    # an - nth term, sn - sum of n terms
    # number of terms (n) below max value = (max value) // (d)
    # an = (a1) + (n - 1)*d
    # sn = (n * (a1 + an))/2    
    no_of_terms = max_value // factor
    last_multiple = factor + (no_of_terms - 1) * factor
    total = (no_of_terms * (factor + last_multiple))/2
    print(f'sum of multiples of {factor} under {max_value} is {total}')
    return round(total)

def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())

        # Method 1 - This method works for smaller values
        # For larger max value, memory issues crop up
        # multiples = [ i for i in range(n) if i % 3 == 0 or i % 5 == 0 ]
        # #print(multiples)        
        # sum = 0
        # for i in multiples:
        #     sum += i
        # print(sum)

        # Method 2 - Generator Expression
        # The list of multiples or provided one by one without storing the 
        # entire list in memory. So this approach is memory efficient
        # However still takes much time for larger max values like 10000000
        # result = sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
        # print(result)

        # Method 3 - Arithmetic Progression
        # This is the fastest and memory efficient approach
        print(sum_of_multiples(n - 1, 3) + sum_of_multiples(n - 1, 5) - sum_of_multiples(n - 1 ,15))

if __name__ == '__main__':
    main()