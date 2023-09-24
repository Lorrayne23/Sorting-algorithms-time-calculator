import random
from mergesort import MergeSort
import time
from quicksort import QuickSort

class AlgorithmsExecution:
    def __init__(self):
        self.vectorSizes = [62500, 125000, 250000, 375000]
        self.timeExecutionMergeSort = []
        self.timeExecutionQuickSort = []
        self.averageTimesMergeSort = []
        self.averageTimesQuickSort = []

    def runDefinedValues(self):
        for size in self.vectorSizes:
            print(str(size))
            for _ in range(50):
                aleatoryVector = [random.randint(1, 100) for _ in range(size)]
                self.mergeSortExecution(aleatoryVector)
                self.quickSortExecution(aleatoryVector)
            self.averageMergeSortExecution()
            self.averageQuickSortExecution()
        self.defineDictVectorsTime(self.averageTimesMergeSort)
        self.defineDictVectorsTime(self.averageTimesQuickSort)

    def mergeSortExecution(self,vector):
        start_time = time.time()
        merge_sort = MergeSort().sort(vector)
        end_time = time.time()
        execution_time = end_time - start_time
        self.timeExecutionMergeSort.append(execution_time)

    def quickSortExecution(self,vector):
        start_time = time.time()
        quick_sort = QuickSort().sort(vector)
        end_time = time.time()
        execution_time = end_time - start_time
        self.timeExecutionQuickSort.append(execution_time)

    def averageMergeSortExecution(self):
        print(self.timeExecutionMergeSort)
        average = sum(self.timeExecutionMergeSort) / len(self.timeExecutionMergeSort)
        self.averageTimesMergeSort.append(average)
        print("Average execution time Merge Sort algorithm:", average)
        self.timeExecutionMergeSort = []


    def averageQuickSortExecution(self):
        print(self.timeExecutionQuickSort)
        average = sum(self.timeExecutionQuickSort) / len(self.timeExecutionQuickSort)
        self.averageTimesQuickSort.append(average)
        print("Average execution time Quick Sort algorithm:", average)
        self.timeExecutionQuickSort = []

    def defineDictVectorsTime(self,averageTimes):
        size_time = {self.vectorSizes[i]: averageTimes[i] for i in range(len(self.vectorSizes))}
        print(size_time)


if __name__ == "__main__":
    algorithms_time = AlgorithmsExecution()
    algorithms_time.runDefinedValues()



