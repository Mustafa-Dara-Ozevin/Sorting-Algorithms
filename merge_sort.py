def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array)//2

        left = array[:midpoint]
        right = array[midpoint:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1
        
""" 

test_array = [20, 77, 14, 7, 22, 31, 96, 8, 1, 9, 35,67,5,76,2,6,56,37,12,66,47,3,4]
merge_sort(test_array)
print(test_array)"""