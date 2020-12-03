def insertionsort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            print(array)
            i -= 1
        array[i+1] = key

test_array = [4,2,8,9,5,6,3,8]
#print(f'array before sort: {test_array}')
#insertionsort(test_array)
#print(f'array after sort: {test_array}')