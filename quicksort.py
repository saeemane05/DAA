import random

comparisons = 0


def partition(arr, low, high, random_pivot):

    global comparisons

    if random_pivot == True:
        p = random.randint(low, high)

        temp = arr[p]
        arr[p] = arr[high]
        arr[high] = temp

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        comparisons = comparisons + 1

        if arr[j] <= pivot:

            i = i + 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1


# Quick Sort Function
def quick_sort(arr, low, high, random_pivot):

    if low < high:

        p = partition(arr, low, high, random_pivot)

        quick_sort(arr, low, p - 1, random_pivot)
        quick_sort(arr, p + 1, high, random_pivot)


# User Input
numbers = input("Enter numbers separated by spaces: ")
numbers = numbers.split()

arr = []

for x in numbers:
    arr.append(int(x))


# Deterministic Quick Sort
a = arr.copy()
comparisons = 0

quick_sort(a, 0, len(a) - 1, False)

print("Deterministic Quick Sort:")
print("Sorted List:", a)
print("Comparisons:", comparisons)


# Randomized Quick Sort
b = arr.copy()
comparisons = 0

quick_sort(b, 0, len(b) - 1, True)

print("Randomized Quick Sort:")
print("Sorted List:", b)
print("Comparisons:", comparisons)