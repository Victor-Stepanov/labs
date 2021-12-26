import random as rd
import time as tm

rd.seed()


def BinarySearch(arr, l, r, x):
    """Binary search function.

    Args:
        arr: list with elements
        l: Number of the first element
        r: Number of the last element
        x: value which will be searched
    Returns:
        number of the array element if its found, otherwise returns value = -1
    """
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return BinarySearch(arr, l, mid - 1, x)
        else:

            return BinarySearch(arr, mid + 1, r, x)
    else:
        return -1


def partition(start, end, array):
    """Helper function for quick sort: gets the pivot element.

    Args:
        start: Number of the first element
        end: Number of the last element
        array: list with elements
    Returns:
        number of the pivot element
    """
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if (start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end


def QuickSort(start, end, array):
    """Quick sort function: sorts list from arguments

    Args:
        start: Number of the first element
        end: Number of the last element
        array: list with elements
    """
    if (start < end):
        p = partition(start, end, array)

        QuickSort(start, p - 1, array)

        QuickSort(p + 1, end, array)


def BubbleSort(arr):
    """Bubble sort function: sorts list from arguments

    Args:
        arr: list with elements
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


def BogoSort(arr):
    """Permutation sort function: sorts list from arguments

    Args:
        arr: list with elements
    """

    def correct(arr):
        s = len(arr) - 1
        while s > 0:
            if arr[s - 1] > arr[s]:
                return 0
            s -= 1
        return 1

    def shuffle(arr):
        for i in range(len(arr)):
            j = rd.randint(0, len(arr) - 1)
            arr[i], arr[j] = arr[j], arr[i]

    while correct(arr) == 0:
        shuffle(arr)


def CountingSort(arr):
    """Counting sort algorithm function: sorts list from arguments

    Args:
        arr: list with elements
    """
    size = 255
    b = [0] * len(arr)
    c = [0] * (size + 1)
    for i in range(len(arr)):
        c[ord(arr[i])] += 1
    for i in range(1, size, 1):
        c[i] += c[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        b[c[ord(arr[i])] - 1] = arr[i]
        c[ord(arr[i])] -= 1
    return b


def test():
    """Function to get timing for QuickSort and BubbleSort algorithms functions: generates test data and gets timings
    for sorting functions

    Returns:
        list with average times for QuickSort and BubbleSort algorithms functions
    """
    res = []
    for n in [10, 100, 1000, 10000, 100000]:
        avgtime2 = 0
        avgtime4 = 0
        for t in range(10):

            data = [rd.randint(-50, 50) for _ in range(n)]

            start = tm.time()
            QuickSort(0, len(data) - 1, data)
            avgtime2 += tm.time() - start

            data = [rd.randint(-50, 50) for _ in range(n)]
            start = tm.time()
            BubbleSort(data)
            avgtime4 += tm.time() - start
        res.append([avgtime2 / 10.0, avgtime4 / 10.0])
    return res



