# RECURSION
# This is an algorithmic concept that involves splitting a problem into 
# two parts: a base case and a recursive case. 
# The problem is divided into smaller subproblems which are then solved
# recursively until such time as they are small enough and meet some base case;
# once the base case is met, the solutions for each subproblem are combined and 
# their result is the answer to the entire problem.

# If the base case is not met, the function's recursive case calls the 
# function again with modified values. The code must be structured in such a way
# that the base case is reachable after some number of iterations, meaning that 
# each subsequent modified value should bring you closer and closer to the base 
# case; otherwise, you'll be stuck in the dreaded infinite loop!

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    print(factorial(int(input('n: '))))


if __name__ == '__main__':
    main()