# Quick Sort (fixed and standard implementation)

arr = [2, 33, 3, 11, 4, 6, 5, 87, 66, 1, 9]

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

print("Before sorting:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)


# Merge Sort implementation

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge the temp arrays back into arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage:
arr2 = [12, 11, 13, 5, 6, 7]
print("Before merge sort:", arr2)
merge_sort(arr2)
print("After merge sort:", arr2)


# Heap Sort implementation

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

# Example usage:
arr3 = [4, 10, 3, 5, 1]
print("Before heap sort:", arr3)
heap_sort(arr3)
print("After heap sort:", arr3)