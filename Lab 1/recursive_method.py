import time
import matplotlib.pyplot as plt
import sys

# Track recursion depth
recursion_depth = 0
max_recursion_depth = 0


def nth_fibonacci(n):
    """Naïve recursive Fibonacci implementation with space complexity tracking"""
    global recursion_depth, max_recursion_depth
    recursion_depth += 1
    max_recursion_depth = max(max_recursion_depth, recursion_depth)  # Track max depth

    if n <= 1:
        recursion_depth -= 1
        return n

    # Recursive case: sum of the two preceding Fibonacci numbers
    result = nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
    recursion_depth -= 1
    return result


# List of Fibonacci terms to compute
n_values = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
execution_times = []
space_complexities = []  # Store max recursion depth

# Compute Fibonacci numbers, measure execution time and space complexity
print("Fibonacci Term | Computation Time (seconds) | Space Complexity (Max Recursion Depth)")
print("-------------------------------------------------------------------------")

for n in n_values:
    max_recursion_depth = 0  # Reset max recursion depth before each call

    start_time = time.time()
    nth_fibonacci(n)  # Compute Fibonacci(n) recursively (ignoring result)
    end_time = time.time()
    execution_time = end_time - start_time  # Compute elapsed time

    execution_times.append(execution_time)
    space_complexities.append(max_recursion_depth)  # Store max recursion depth

    # Print result with space complexity
    print(f"Fibonacci({n}), Time: {execution_time:.6f} sec, Space: {max_recursion_depth}")

# Plot the execution time graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, execution_times, marker='o', linestyle='-', color='b', label="Execution Time")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time (s)")
plt.title("Recursive Fibonacci Function")
plt.legend()
plt.grid(True)
plt.show()

# Plot space complexity graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, space_complexities, marker='o', linestyle='-', color='r', label="Max Recursion Depth")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Recursion Depth")
plt.title("Space Complexity of Recursive Fibonacci")
plt.legend()
plt.grid(True)
plt.show()
