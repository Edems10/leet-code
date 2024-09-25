import random
from timeit import timeit
from typing import List
import numpy

class QuickSort:
    def __init__(self,array_to_sort) -> None:
        self.array = array_to_sort
        if not self.checkArrayExists():
            raise ValueError("Not valid array to sort")
    
    def numpyQuickSort(self)-> List[int]:
        return numpy.sort(self.array,kind='quicksort')
        
    def checkArrayExists(self)->bool:
        if self.array !=None and len(self.array)>1:
            return True
        return False    
        
    def myQuickSortImplementation(self,array):
        if len(array)<=1:
            return array
        
        pivot = array[0]
        s_array = []
        b_array = []
        for x in array[1:]:
            if x<pivot:
                s_array.append(x)
            else:
                b_array.append(x)
        return self.myQuickSortImplementation(s_array) +[pivot]+ self.myQuickSortImplementation(b_array)


        
            
def generate_random_array(size:int) -> List[int]:
    return [random.randint(0,100) for _ in range(size)]

def wrapperNumpyQuickSort(qs:QuickSort):
    """Function to wrap the quicksort call for timeit."""
    qs.numpyQuickSort()

def wrapperMyQuickSort(qs:QuickSort):
    """Function to wrap the quicksort call for timeit."""
    qs.myQuickSortImplementation(qs.array)
        

def main():
    qs = QuickSort(generate_random_array(10000))
    execution_time = timeit(lambda: wrapperNumpyQuickSort(qs), number=1000)
    print(f"Numpy Quicksort took {execution_time:.6f} seconds for 1000 runs for array of size {len(qs.array)}")
    execution_time = timeit(lambda: wrapperMyQuickSort(qs), number=1000)
    print(f"My Quicksort took {execution_time:.6f} seconds for 1000 runs for array of size {len(qs.array)}")



if __name__ =="__main__":
    main()


