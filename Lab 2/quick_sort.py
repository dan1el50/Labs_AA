def median_of_three(array, low, high):
    """Sorts the first, middle, and last elements and returns the index of the median."""
    mid = (low + high) // 2

    if array[low] > array[mid]:
        array[low], array[mid] = array[mid], array[low]
    if array[mid] > array[high]:
        array[mid], array[high] = array[high], array[mid]
    if array[low] > array[mid]:
        array[low], array[mid] = array[mid], array[low]
    return mid

def partition(array, low, high):
    """Partition function that handles duplicate elements better."""
    pivot_index = median_of_three(array, low, high)
    pivot = array[pivot_index]
    array[pivot_index], array[high] = array[high], array[pivot_index]

    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    """QuickSort using Median-of-Three pivot selection."""
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


