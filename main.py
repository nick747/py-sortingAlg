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
