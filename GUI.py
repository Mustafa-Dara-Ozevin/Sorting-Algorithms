import random
import tkinter as tk


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.generate_array = tk.Button(
            text='Generate array', command=self.array_generator)
        self.generate_array.pack()

        self.sort_array = tk.Button(
            text='Sort array', command=self.array_sorter)
        self.sort_array.pack()

        self.array_label = tk.Label()
        self.array_label.pack()

        self.sorting_label = tk.Label()
        self.sorting_label.pack()

        OPTIONS = ['bubble_sort_optimized', "bubble_sort_unoptimized",
                   "bubble_sort_cut_extra_loops", "comb_sort",
                   "selection_sort", "shell_sort"]

        self.variable = tk.StringVar(self.parent)
        self.variable.set(OPTIONS[0])  # default value
        algorithm_selector = tk.OptionMenu(
            self.parent, self.variable, *OPTIONS)
        algorithm_selector.pack()

    def array_generator(self):
        self.generate_array['text'] = 'Generating...'
        self.array = []
        for i in range(20):  # decrease array length here
            self.array.append(random.randint(0, 500))
        self.array_label['text'] = f'{self.array}'
        self.generate_array['text'] = 'Generate again'

    def array_sorter(self):
        self.sorting_label['text'] = 'Sorting preview'
        eval(f'self.{str(self.variable.get())}()')

    def bubble_sort_optimized(self):
        has_swapped = True
        iter_count = 0
        while has_swapped:
            self.sorting_label['text'] += f'\n{self.array}'
            has_swapped = False
            for i in range(len(self.array)-iter_count-1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i +
                                              1] = self.array[i+1], self.array[i]
                    has_swapped = True
            iter_count += 1

    def bubble_sort_unoptimized(self):
        for j in range(len(self.array)):
            self.sorting_label['text'] += f'\n{self.array}'
            for i in range(len(self.array)-1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i +
                                              1] = self.array[i+1], self.array[i]

    def bubble_sort_cut_extra_loops(self):
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for i in range(len(self.array)-1):
                self.sorting_label['text'] += f'\n{self.array}'
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i +
                                              1] = self.array[i+1], self.array[i]
                    has_swapped = True

    def get_gap(self, gap):
        gap = (gap*10)/13
        if gap < 1:
            return 1
        return int(gap)

    def comb_sort(self):
        n = len(self.array)
        gap = n
        has_swapped = True
        while has_swapped or gap != 1:
            self.sorting_label['text'] += f'\n{self.array}'
            gap = self.get_gap(gap)
            has_swapped = False
            for i in range(len(self.array)-gap):
                if self.array[i] > self.array[i+gap]:
                    self.array[i], self.array[i +
                                              gap] = self.array[i+gap], self.array[i]
                    has_swapped = True

    def insertion_sort(self):
        for j in range(1, len(self.array)):
            self.sorting_label['text'] += f'\n{self.array}'
            key = self.array[j]
            i = j - 1
            while i >= 0 and self.array[i] > key:
                self.array[i+1] = self.array[i]
                i -= 1
            self.array[i+1] = key

    def selection_sort(self):
        for i in range(len(self.array)):
            self.sorting_label['text'] += f'\n{self.array}'
            min_index = i
            for j in range(min_index+1, len(self.array)):
                if self.array[min_index] > self.array[j]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

    def shell_sort(self):
        n = len(self.array)
        gap = n // 2

        while gap > 0:
            self.sorting_label['text'] += f'\n{self.array}'
            for i in range(gap, len(self.array)):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j-gap] > temp:
                    self.array[j] = self.array[j-gap]
                    j -= gap

                self.array[j] = temp
            gap //= 2


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
