import random
from mergesort import MergeSort
from selectionsort import Selection
import time

class AlgorithmsExecution:
    def __init__(self):
        self.vectorSizes = [62500, 125000, 250000, 375000]
        self.timeExecutionMergeSort = []

    def runDefinedValues(self):
        for size in self.vectorSizes:
            for _ in range(50):
                print(str(size))
                aleatoryVector = [random.randint(1, 100) for _ in range(size)]
                self.mergeSortExecution(aleatoryVector)
                #selection_order = Selection().selectionSort(aleatoryVector)
                #print("Selection Sort Order:", selection_order)

    def mergeSortExecution(self,vector):
        start_time = time.time()
        merge_sort = MergeSort().sort(vector)
        end_time = time.time()
        execution_time = end_time - start_time
        self.timeExecutionMergeSort.append(execution_time)

    def averageMergeSortExecution(self):
        average = sum(self.timeExecutionMergeSort) / len(self.timeExecutionMergeSort)
        print("Average execution time Merge Sort algorithm:", average)


if __name__ == "__main__":
    benchmark = AlgorithmsExecution()
    benchmark.runDefinedValues()
    benchmark.averageMergeSortExecution()


