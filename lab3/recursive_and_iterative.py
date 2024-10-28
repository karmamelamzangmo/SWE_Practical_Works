def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return [0] if n == 0 else [0, 1][:n]
    
    fib_sequence = [0, 1]
    for _ in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def find_fibonacci_index_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

def is_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

def fibonacci_ratios(limit):
    a, b = 0, 1
    ratios = []
    for _ in range(limit):
        if b != 0:
            ratios.append(a / b)
        a, b = b, a + b
    return ratios

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test the functions

# 1. Modified iterative function.
n = 10
fib_sequence = fibonacci_iterative(n)
print(f"Fibonacci sequence up to F({n}): {fib_sequence}")

# 2. Finding the index of the first Fibonacci number that exceeds a given value
value = 100
index_exceeding_value = find_fibonacci_index_exceeding(value)
print(f"Index of first Fibonacci number exceeding {value}: {index_exceeding_value}")

# 3. Determining if a number is a Fibonacci number
test_number = 21
is_fib = is_fibonacci(test_number)
print(f"Is {test_number} a Fibonacci number? {is_fib}")

# 4. Calculating the ratio between consecutive Fibonacci numbers
ratios = fibonacci_ratios(10)
print("Ratios between consecutive Fibonacci numbers:", ratios)

# Compare recursive, iterative, and memoized performance
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(lambda n: fibonacci_iterative(n)[-1], n)
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

