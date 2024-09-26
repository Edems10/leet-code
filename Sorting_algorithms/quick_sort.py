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
