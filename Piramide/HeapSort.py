from heapify import *
from interface import *
import random


def heap_sort(arr):
    n = len(arr)

    print("Building the heap...")
    for max_index in range(n // 2 - 1, -1, - 1):
        heapify(arr, n, max_index)

    print("Sorting the elements:")
    for max_index in range(n - 1, 0, -1):
        arr[0], arr[max_index] = arr[max_index], arr[0]
        print_heap(arr)
        heapify(arr, max_index, 0)


n = int(input("Enter number of elements:"))
arr = [random.randint(1, 1000000) for _ in range(n)]

print("Unsorted array:", arr)
print_heap(arr)

heap_sort(arr)
print("Sorted array:", arr)
