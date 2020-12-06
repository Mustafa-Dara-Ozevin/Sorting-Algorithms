def get_gap(gap):
    gap = (gap*10)/13
    if gap < 1:
        return 1
    return int(gap)

def comb_sort(array):
    n = len(array)
    gap = n
    has_swapped = True
    while has_swapped or gap != 1:
        gap = get_gap(gap)
        has_swapped = False
        for i in range(len(array)-gap):
            if array[i] > array[i+gap]:
                array[i],array[i+gap] = array[i+gap],array[i]
                has_swapped = True

test_array = [20, 77, 14, 7, 22, 31, 96, 8, 1, 9, 35,67,5,76,2,6,56,37,12,66,47,3,4]
comb_sort(test_array)
print(test_array)