# PYTHON SORTING ALGORITHMS - TEST
import random


# Generate random array
def generateArray():
    array = []
    length = int(input("Give a length to the generated array: "))
    for i in range(length):
        array.append(random.randint(0, 100))  # put a max value here

    return array


# Bubble Sort
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print("Sorted with Bubble Sort: ", array)


# Selection Sort
def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if array[j] < array[min_i]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]

    print("Sorted with Selection Sort: ", array)


# Insertion Sort
def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    print("Sorted with Insertion Sort: ", array)


# Merge Sort
def mergeSort(array):
    if len(array) <= 1:
        array = array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    array = merge(left, right)
    print("Sorted with Merge Sort: ", array)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Quick Sort
def quickSort(array):
    if len(array) <= 1:
        array = array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    array = quickSort(left) + middle + quickSort(right)
    print("Sorted with Quick Sort: ", array)


# Heap Sort
def heapSort(array):
    def heapify(array, n, i):
        max = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[i] < array[left]:
            max = left
        if right < n and array[max] < array[right]:
            max = right
        if max != i:
            array[i], array[max] = array[max], array[i]
            heapify(array, n, max)

    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        array = heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        arrau = heapify(array, i, 0)

    print("Sorted with Heap Sort: ", array)


# Counting Sort
def countingSort(array):
    max = max(array)
    count = [0] * (max + 1)
    for num in array:
        count[num] += 1
    sorted = []
    for i in range(len(count)):
        sorted.extend([i] * count[i])
    array = sorted
    print("Sorted with Counting Sort: ", array)


def main():
    numbers = generateArray()
    print("Generated array: ", numbers)
    choice = int(input(
        "Choose the sort you wanna do (1. Bubble, 2. Selection, 3. Insertion, 4. Merge, 5. Quick, 6. Heap, 7. Counting): "))
    if (choice == 1):
        bubbleSort(numbers)
    elif (choice == 2):
        selectionSort(numbers)
    elif (choice == 3):
        insertionSort(numbers)
    elif (choice == 4):
        mergeSort(numbers)
    elif (choice == 5):
        quickSort(numbers)
    elif (choice == 6):
        heapSort(numbers)
    elif (choice == 7):
        countingSort(numbers)
    else:
        print("Error: input must be a number between 1 and 7")


main()
