import timeit
import random
#code can take a while to finish if you want a faster runtime
#either lower the length of the array or number of repeats in timeit function

def compare_sort_speed(func_list, array):
    setup = """
from bubble_sort import bubble_sort_optimized, bubble_sort_unoptimized, bubble_sort_cut_extra_loops
from  comb_sort import comb_sort 
from  insertion_sort import insertion_sort
from  merge_sort import merge_sort
from  selection_sort import selection_sort
from  shell_sort import shell_sort
"""
    for func in func_list:
        code = f"""
{func}({array})
"""
        time = round(timeit.timeit(code, setup=setup, number=2),3) #decrease number of repeats here
        print(f'sort time of {func} is: {time}')


array = []
for i in range(5000): # decrease array length here
    array.append(random.randint(0,500))


func_list = ['bubble_sort_optimized', "bubble_sort_unoptimized",
             "bubble_sort_cut_extra_loops","comb_sort", 'merge_sort',
             "selection_sort", "shell_sort" ]
compare_sort_speed(func_list, array)
