import random
import tkinter as tk
import threading
import time


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.c = tk.Canvas(self.parent,width=600, height=251)
        self.c.pack()
        self.array = []



        self.generate_array = tk.Button(
            text='Generate array', command=self.array_generator)
        self.generate_array.pack()

        self.sort_array = tk.Button(
            text='Sort array', command=self.start)
        self.sort_array.pack()

        self.array_label = tk.Label()
        self.array_label.pack()

        self.sorting_label = tk.Label()
        self.sorting_label.pack()

        OPTIONS = ['bubble_sort_optimized', "bubble_sort_unoptimized",
                   "bubble_sort_cut_extra_loops", "insertion_sort", "comb_sort",
                   "selection_sort", "shell_sort"]

        self.variable = tk.StringVar(self.parent)
        self.variable.set(OPTIONS[0])  # default value
        algorithm_selector = tk.OptionMenu(
            self.parent, self.variable, *OPTIONS)
        algorithm_selector.pack()

    def array_generator(self):
        self.array = []

        for i in range(1,251):  # decrease array length here
            self.array.append(i)
        
        random.shuffle(self.array)
        self.visualize()
        self.generate_array['text'] = 'Generate again'
    
    def refresh(self):
        self.parent.update()
        self.parent.after(1000,self.refresh)
    
    def start(self):
        self.refresh()
        threading.Thread(target=self.array_sorter).start()


    
    def visualize(self):
        self.c.delete("all")
        self.rectangles = {}
        for i in range(len(self.array)):
            self.rectangles["key%s"%i] = self.c.create_rectangle(i*2+5,0,i*2+6,self.array[i],outline="blue")
        time.sleep(0.01)

    def refresh_graph(self,x,y):
        self.c.delete(self.rectangles["key%s"%x])
        self.rectangles["key%s"%x] = self.c.create_rectangle(x*2+5,0,x*2+6,self.array[x],outline="red")
        self.c.delete(self.rectangles["key%s"%y])
        self.rectangles["key%s"%y] = self.c.create_rectangle(y*2+5,0,y*2+6,self.array[y],outline="red")
        self.c.itemconfig(self.rectangles["key%s"%x],outline="blue")
        self.c.itemconfig(self.rectangles["key%s"%y],outline="blue")

    def array_sorter(self):
        self.sorting_label['text'] = 'Sorting preview'
        eval(f'self.{str(self.variable.get())}()')

    def bubble_sort_optimized(self):
        has_swapped = True
        iter_count = 0
        while has_swapped:
            has_swapped = False
            for i in range(len(self.array)-iter_count-1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i +
                                              1] = self.array[i+1], self.array[i]
                    self.refresh_graph(i,i+1)
                    has_swapped = True
            iter_count += 1
            

    def bubble_sort_unoptimized(self):
        for j in range(len(self.array)):
            for i in range(len(self.array)-1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i +
                                              1] = self.array[i+1], self.array[i]
                    self.refresh_graph(i,i+1)

    def bubble_sort_cut_extra_loops(self):
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for i in range(len(self.array)-1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i +
                                              1] = self.array[i+1], self.array[i]
                    self.refresh_graph(i,i+1)
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
            gap = self.get_gap(gap)
            has_swapped = False
            for i in range(len(self.array)-gap):
                if self.array[i] > self.array[i+gap]:
                    self.array[i], self.array[i +
                                              gap] = self.array[i+gap], self.array[i]
                    self.refresh_graph(i,i+gap)
                    has_swapped = True

    def insertion_sort(self):
        for j in range(1, len(self.array)):
            key = self.array[j]
            i = j - 1
            while i >= 0 and self.array[i] > key:
                self.array[i+1] = self.array[i]
                self.refresh_graph(i+1,i)
                i -= 1
            self.array[i+1] = key
            self.refresh_graph(i+1,i+1)
            

    def selection_sort(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(min_index+1, len(self.array)):
                if self.array[min_index] > self.array[j]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.refresh_graph(i,min_index)

    def shell_sort(self):
        n = len(self.array)
        gap = n // 2

        while gap > 0:
            for i in range(gap, len(self.array)):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j-gap] > temp:
                    self.array[j] = self.array[j-gap]
                    self.refresh_graph(j,j-gap)
                    j -= gap
                self.array[j] = temp
                self.refresh_graph(j,j)
            gap //= 2

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
