import time
import matplotlib.pyplot as plt
from functools import lru_cache

# Recursive Fibonacci with Memoization
@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    """Recursive Fibonacci using memoization (Top-Down DP)"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

# List of Fibonacci terms to compute
n_values = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
execution_times = []
fibonacci_results = []

# Compute Fibonacci numbers, measure execution time, and print results
print("Fibonacci Term | Computation Time (seconds)")
print("------------------------------------------")

for n in n_values:
    start_time = time.time()
    result = fibonacci_memoized(n)  # Compute Fibonacci(n) using memoization
    end_time = time.time()
    execution_time = end_time - start_time  # Compute elapsed time

    execution_times.append(execution_time)
    fibonacci_results.append(result)

    # Print result
    print(f"Fibonacci({n}) = {result}, Time: {execution_time:.6f} sec")

# Plot the execution time graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, execution_times, marker='o', linestyle='-', color='g', label="Execution Time (Memoized)")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time (s)")
plt.title("Memoized Fibonacci Function (Top-Down DP)")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
