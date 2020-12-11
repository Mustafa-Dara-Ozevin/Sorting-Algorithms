def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(min_index+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
        
        array[i],array[min_index] = array[min_index],array[i]
"""
test_array = [8,2,5,1,6,3,9,15,0,32,1]
selection_sort(test_array)
print(test_array)"""