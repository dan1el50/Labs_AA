import time
import matplotlib.pyplot as plt
import math
import sys


def fibonacci_binet(n):
    """Computes Fibonacci(n) using Binet's Formula (Closed-Form Expression)"""
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    result = round((phi ** n - psi ** n) / sqrt_5)  # Rounding to avoid floating-point errors

    # Space complexity calculation (sum of memory used by key variables)
    space_usage = sys.getsizeof(n) + sys.getsizeof(sqrt_5) + sys.getsizeof(phi) + sys.getsizeof(psi) + sys.getsizeof(result)
    return space_usage  # Return only memory usage (ignoring the result)


# List of Fibonacci terms to compute
n_values = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
execution_times_s = []  # Store execution times in seconds
space_usages = []  # Store space complexity results

# Compute Fibonacci numbers, measure execution time and space complexity
print("Fibonacci Term | Computation Time (seconds) | Space Complexity (bytes)")
print("-------------------------------------------------------------")

for n in n_values:
    # Time in seconds
    start_time_s = time.time()
    space_used = fibonacci_binet(n)  # Compute space usage (ignore result)
    end_time_s = time.time()
    execution_time_s = end_time_s - start_time_s  # Compute elapsed time in seconds

    execution_times_s.append(execution_time_s)  # Store execution time
    space_usages.append(space_used)  # Store space usage

    # Print result with space complexity (without the Fibonacci value)
    print(f"Fibonacci({n}), Time: {execution_time_s:.10f} sec, Space: {space_used} bytes")

# Plot the execution time graph (in seconds) with **linear scale**
plt.figure(figsize=(8, 5))
plt.plot(n_values, execution_times_s, marker='o', linestyle='-', color='c', label="Execution Time (Binet's Formula)")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time (seconds)")
plt.title("Binet's Formula Fibonacci Function (Closed-Form)")
plt.legend()
plt.grid(True)
plt.show()

# Plot the space complexity graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, space_usages, marker='o', linestyle='-', color='r', label="Space Complexity (Binet's Formula)")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Memory (bytes)")
plt.title("Space Complexity of Binet's Formula")
plt.legend()
plt.grid(True)
plt.show()
