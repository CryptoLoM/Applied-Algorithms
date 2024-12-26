def print_heap(arr):
    n = len(arr)
    level = 0
    i = 0
    while i < n:
        start = i
        end = min(i + 2**level, n)
        print("Level", level, ":", arr[start:end])
        i = end
        level += 1
    print()
