import heapq
from interface import *


priority_queue = []

# Додавання елементів у чергу
heapq.heappush(priority_queue, (4, "element 2"))
heapq.heappush(priority_queue, (2, "element 0"))
heapq.heappush(priority_queue, (3, "element 1"))
heapq.heappush(priority_queue, (1, "element -5"))
heapq.heappush(priority_queue, (2, "element 0"))

# Отримання елемента з найвищим пріоритетом
while priority_queue:
    priority = heapq.heappop(priority_queue)
    print(f"Priority: {priority[0]}, Queue: {priority[1]}")


def heapify(arr, n, el_with_maxindex):
    largest = el_with_maxindex
    left = el_with_maxindex * 2 + 1
    right = el_with_maxindex * 2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != el_with_maxindex:
        arr[el_with_maxindex], arr[largest] = arr[largest], arr[el_with_maxindex]
        print_heap(arr)
        heapify(arr, n, largest)
