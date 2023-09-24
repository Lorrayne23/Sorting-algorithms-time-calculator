import random
from mergesort import MergeSort
from selectionsort import Selection
import time

class AlgorithmsExecution:
    def __init__(self):
        self.vectorSizes = [62500, 125000, 250000, 375000]
        self.timeExecution = []
        self.averageTimes = []

    def runDefinedValues(self):
        for size in self.vectorSizes:
            print(str(size))
            for _ in range(10):
                aleatoryVector = [random.randint(1, 100) for _ in range(size)]
                self.mergeSortExecution(aleatoryVector)
            self.averageMergeSortExecution()
        print(self.averageTimes)

    def mergeSortExecution(self,vector):
        start_time = time.time()
        merge_sort = MergeSort().sort(vector)
        end_time = time.time()
        execution_time = end_time - start_time
        self.timeExecution.append(execution_time)


    def averageMergeSortExecution(self):
        print(self.timeExecution)
        average = sum(self.timeExecution) / len(self.timeExecution)
        self.averageTimes.append(average)
        print("Average execution time Merge Sort algorithm:", average)
        self.timeExecution = []

    def defineDictVectorsTime(self):
        size_time = {}
        for i in range(len(self.vectorSizes)):
            size = self.vectorSizes[i]
            time = self.averageTimes[i]
            size_time[size] = time  #  o tamanho à média de tempo no dicionário

        # Exibindo o dicionário resultante
        print(size_time)


if __name__ == "__main__":
    benchmark = AlgorithmsExecution()
    benchmark.runDefinedValues()
    benchmark.defineDictVectorsTime()
    #benchmark.averageMergeSortExecution()


