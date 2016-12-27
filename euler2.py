'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.

By starting with 1 and 2, the first 10 terms will be:

  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

  By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
memo = {0:0, 1:1}

def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def even(n): return n % 2 == 0

def fib_array(max_number):
    array = []
    n = 1

    while max_number > fib(n):
        array.append(fib(n))
        n += 1

    return array

if __name__ == "__main__":
    print(sum(filter(even,fib_array(4000000))))