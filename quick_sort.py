# Takes the last item as pivot and places it into correct position
# all elements smaller then pivot goes to left of pivot
# and all elements bigger then goes to left of pivot
def partition(array, low, high):
    pivot = array[high]
    i = low-1 

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

# low = starting index
# high = ending index

def quicksort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:

        pivot = partition(array, low, high)

        quicksort(array, low, pivot-1)
        quicksort(array, pivot+1, high)


test_array = [377, 3, 9, 6, 76, 8, 1, 2, 5, 27, 7, 4]
quicksort(test_array, 0, len(test_array)-1)
print(test_array)
