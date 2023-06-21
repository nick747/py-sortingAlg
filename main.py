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

# Merge Sort


def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)


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
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left) + middle + quickSort(right)
