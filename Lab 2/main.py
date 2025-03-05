import random
import sys
import matplotlib.pyplot as plt
from copy import deepcopy
from time import perf_counter

# Import sorting algorithms
from heap_sort import heapSort
from merge_sort import mergeSort
from quick_sort import quickSort
from selection_sort import selection_sort

# Set recursion limit for QuickSort
sys.setrecursionlimit(10**7)

# Sorting function wrapper for QuickSort and MergeSort
def quickSortWrapper(arr):
    quickSort(arr, 0, len(arr) - 1)

def mergeSortWrapper(arr):
    mergeSort(arr, 0, len(arr) - 1)

# Function to measure execution time
def measure_time(sort_function, arr, runs=5):
    total_time = 0
    for _ in range(runs):
        test_arr = deepcopy(arr)  # Prevent modifying the original array
        start_time = perf_counter()
        sort_function(test_arr)
        total_time += (perf_counter() - start_time)
    return total_time / runs  # Return average execution time

# Array sizes for testing
sizes = [100, 500, 1000, 5000, 10000]

# Test cases (Generated for each size)
def generate_test_cases(size):
    return {
        "General Unsorted": [random.randint(-10000, 10000) for _ in range(size)],
        "Already Sorted": list(range(1, size + 1)),
        "Reverse Sorted": list(range(size, 0, -1)),
        "Array with Duplicates": [random.randint(-100, 100) for _ in range(size)],
    }

# Sorting algorithms and their labels
sorting_algorithms = {
    "QuickSort": quickSortWrapper,
    "MergeSort": mergeSortWrapper,
    "HeapSort": heapSort,
    "SelectionSort": selection_sort,
}

# Store results for plotting
results = {alg: {case: [] for case in generate_test_cases(10)} for alg in sorting_algorithms}

# Run tests for all sorting algorithms
def main():
    print("\n--- Sorting Algorithm Performance Test ---")
    for size in sizes:
        print(f"\n--- Array Size: {size} ---")
        test_cases = generate_test_cases(size)
        for alg_name, sort_function in sorting_algorithms.items():
            print(f"\n{alg_name} Results:")
            for case_name, arr in test_cases.items():
                runs = 1 if size >= 5000 and alg_name == "SelectionSort" else 5  # Reduce runs for large SelectionSort cases
                execution_time = measure_time(sort_function, arr, runs)
                results[alg_name][case_name].append(execution_time)
                print(f"{case_name}: {execution_time:.6f} seconds")

    # Generate and display graphs
    for alg_name, case_results in results.items():
        plt.figure(figsize=(8, 5))
        for case_name, times in case_results.items():
            plt.plot(sizes, times, marker='o', linestyle='-', label=case_name)

        plt.xlabel("Array Size")
        plt.ylabel("Execution Time (seconds)")
        plt.title(f"{alg_name} Sorting Performance")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    main()
