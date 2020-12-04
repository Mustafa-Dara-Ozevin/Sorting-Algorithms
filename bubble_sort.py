import timeit

def bubble_sort_unoptimized(array):
    for j in range(len(array)):
         for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


# unoptimized bubble sort continues to loop through the array even if the array is sorted.
# To stop that we need to check if we made any swaps or not.
def bubble_sort_cut_extra_loops(array):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        print(array)
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                has_swapped = True

# The way bubble sort works ensures that last n - number_of_iterations item is already sorted.
# So we can cut themm from iteration.
def bubble_sort_optimized(array):
    has_swapped = True
    iter_count = 0
    while has_swapped:
        has_swapped = False
        print(array)
        for i in range(len(array)-iter_count-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                has_swapped = True
        iter_count += 1

test_array = [2, 7, 4, 7, 2, 3, 6, 8, 1, 9, 5,4,5,6,2,6,56,47,12,66,47,3,4]

#print(bubble_sort_unoptimized(test_array))
#print(bubble_sort_cut_extra_loops(test_array))
#print(bubble_sort_optimized(test_array))