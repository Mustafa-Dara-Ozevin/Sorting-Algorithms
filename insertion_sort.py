def insertion_sort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]

            i -= 1
        array[i+1] = key
"""
test_array = [20, 77, 14, 7, 22, 31, 96, 8, 1, 9, 35,67,5,76,2,6,56,37,12,66,47,3,4]
print(f'array before sort: {test_array}')
insertion_sort(test_array)
print(f'array after sort: {test_array}')"""