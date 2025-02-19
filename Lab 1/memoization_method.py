import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000)
# Function to calculate the nth Fibonacci number using memoization
def nth_fibonacci_util(n, memo):
    """Recursive Fibonacci using memoization (Top-Down DP)"""
    if n <= 1:
        return n
    # Check if the result is already in the memo table
    if memo[n] != -1:
        return memo[n]
    # Recursive case: calculate Fibonacci number and store it in memo
    memo[n] = nth_fibonacci_util(n - 1, memo) + nth_fibonacci_util(n - 2, memo)
    return memo[n]

# Wrapper function that handles both initialization and Fibonacci calculation
def nth_fibonacci(n):
    """Wrapper function to initialize memoization table and compute Fibonacci"""
    # Create a memoization table and initialize with -1
    memo = [-1] * (n + 1)
    # Call the utility function
    return nth_fibonacci_util(n, memo)


# List of Fibonacci terms to compute (updated values)
n_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
execution_times_s = []  # Store execution times in seconds
space_usages = []  # Store space complexity results

# Compute Fibonacci numbers, measure execution time and space complexity
print("Fibonacci Term | Computation Time (seconds) | Space Complexity (bytes)")
print("-------------------------------------------------------------")

for n in n_values:
    # Time in seconds
    start_time_s = time.time()
    nth_fibonacci(n)  # Compute Fibonacci number (but ignore result)
    end_time_s = time.time()
    execution_time_s = end_time_s - start_time_s  # Compute elapsed time in seconds

    # Estimate space usage (storing `n+1` integers in the memoization table)
    space_used = sys.getsizeof(n) + sys.getsizeof([-1] * (n + 1))

    execution_times_s.append(execution_time_s)  # Store execution time
    space_usages.append(space_used)  # Store space usage

    # Print result with space complexity (without the Fibonacci value)
    print(f"Fibonacci({n}), Time: {execution_time_s:.10f} sec, Space: {space_used} bytes")

# Plot the execution time graph (in seconds) with **linear scale**
plt.figure(figsize=(8, 5))
plt.plot(n_values, execution_times_s, marker='o', linestyle='-', color='g', label="Execution Time (Memoized DP)")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time (seconds)")
plt.title("Memoized Fibonacci Function (Top-Down DP)")
plt.legend()
plt.grid(True)
plt.show()

# Plot the space complexity graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, space_usages, marker='o', linestyle='-', color='b', label="Space Complexity (Memoized DP)")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Memory (bytes)")
plt.title("Space Complexity of Memoized Fibonacci")
plt.legend()
plt.grid(True)
plt.show()
