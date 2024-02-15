from src.data import arr


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        arr_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        if arr_sorted:
            break
    return array


print(bubble_sort(arr))
