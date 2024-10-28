# Fibonacci Sequence Analyzer

This Python script provides various implementations for calculating Fibonacci numbers, along with additional functionalities such as analyzing performance, generating Fibonacci sequences, and checking properties of Fibonacci numbers.

## Features

- **Recursive Implementation**: Calculate Fibonacci numbers using a recursive approach.
- **Iterative Implementation**: Calculate Fibonacci numbers using an iterative approach and return the entire sequence up to a specified index.
- **Memoized Implementation**: Optimize the recursive calculation of Fibonacci numbers using memoization.
- **Generator Implementation**: Generate Fibonacci numbers up to a specified limit using a generator.
- **Index Finder**: Find the index of the first Fibonacci number that exceeds a given value.
- **Fibonacci Number Checker**: Check if a given number is a Fibonacci number.
- **Ratio Calculator**: Calculate the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.
- **Performance Measurement**: Compare the execution time of different implementations.

## Requirements

- Python 3.x
- No additional libraries are required, as the script uses built-in modules.

## Functions

fibonacci_recursive(n)
Calculates the nth Fibonacci number using recursion.

fibonacci_iterative(n)
Calculates and returns a list of Fibonacci numbers up to the nth Fibonacci number.

fibonacci_generator(limit)
Generates Fibonacci numbers up to a specified limit.

fibonacci_memoized(n, memo={})
Calculates the nth Fibonacci number using memoization to improve performance.

find_fibonacci_index_exceeding(value)
Finds the index of the first Fibonacci number that exceeds a given value.

is_fibonacci(number)
Determines if a given number is a Fibonacci number.

fibonacci_ratios(limit)
Calculates the ratio of consecutive Fibonacci numbers and returns a list of these ratios.

measure_time(func, n)
Measures the execution time of a given function.




