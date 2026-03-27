# Factorial using naive approach
def factorial_naive(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial_naive(n-1)


def factorial(n):

    if n == 0 or n == 1:   
        return 1
    return n * factorial(n - 1)  

# Memoized Recursive Factorial

def factorial_memo(n, memo=None):
    
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return 1

    # Storeing
    memo[n] = n * factorial_memo(n - 1, memo)
    return memo[n]




# Naive Recursive Fibonacci

def fibonacci_naive(n):
    
    if n <= 1:   
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# Memoized Fibonacci

def fibonacci_memo(n, memo=None):
    
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]