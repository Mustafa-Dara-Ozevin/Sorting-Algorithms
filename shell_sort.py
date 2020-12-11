def shell_sort(array):
    
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap,len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap

            array[j] = temp
        gap //= 2
"""
test_array = [20, 77, 14, 7, 22, 31, 96, 8, 1, 9, 35,67,5,76,2,6,56,37,12,66,47,3,4]
print(f'array before sort: {test_array}')
shell_sort(test_array)
print(f'array after sort: {test_array}')

"""