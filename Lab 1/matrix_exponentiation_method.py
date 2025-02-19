import time
import matplotlib.pyplot as plt
import sys
import math

# Function to multiply two 2x2 matrices
def multiply(mat1, mat2):
    """Perform matrix multiplication and update mat1 in-place"""
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    mat1[0][0], mat1[0][1] = x, y
    mat1[1][0], mat1[1][1] = z, w

# Function to perform matrix exponentiation
def matrix_power(mat1, n):
    """Raise matrix mat1 to the power of n using fast exponentiation"""
    if n == 0 or n == 1:
        return

    mat2 = [[1, 1], [1, 0]]  # Helper matrix
    # Recursively calculate mat1^(n // 2)
    matrix_power(mat1, n // 2)
    # Square the matrix mat1
    multiply(mat1, mat1)
    # If n is odd, multiply by the helper matrix mat2
    if n % 2 != 0:
        multiply(mat1, mat2)

# Function to calculate the nth Fibonacci number
def nth_fibonacci(n):
    """Computes Fibonacci(n) using Matrix Exponentiation"""
    if n <= 1:
        return n

    mat1 = [[1, 1], [1, 0]]  # Transformation matrix
    # Raise the matrix mat1 to the power of (n - 1)
    matrix_power(mat1, n - 1)
    return mat1[0][0]  # The result is in the top-left cell of the matrix

# List of Fibonacci terms to compute
n_values = [501, 631, 794, 1000,
1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
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

    # Estimate space usage (memory for matrix and recursion stack depth)
    space_used = sys.getsizeof(n) + sys.getsizeof([[1, 1], [1, 0]]) + (sys.getsizeof(n) * int(math.log2(n)))  # O(log n) depth

    execution_times_s.append(execution_time_s)  # Store execution time
    space_usages.append(space_used)  # Store space usage

    # Print result with space complexity (without the Fibonacci value)
    print(f"Fibonacci({n}), Time: {execution_time_s:.10f} sec, Space: {space_used} bytes")

# Plot the execution time graph (in seconds) with **linear scale**
plt.figure(figsize=(8, 5))
plt.plot(n_values, execution_times_s, marker='o', linestyle='-', color='m', label="Execution Time (Matrix Exponentiation)")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time (seconds)")
plt.title("Matrix Exponentiation Fibonacci Function")
plt.legend()
plt.grid(True)
plt.show()

# Plot the space complexity graph
plt.figure(figsize=(8, 5))
plt.plot(n_values, space_usages, marker='o', linestyle='-', color='r', label="Space Complexity (Matrix Exponentiation)")
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Memory (bytes)")
plt.title("Space Complexity of Matrix Exponentiation")
plt.legend()
plt.grid(True)
plt.show()
