from quicksort import QuickSort
import random
import time

class QuicksortComparison:
    def __init__(self):
        self.timeExecution = []

    def quickSortExecution(self,vector):
        for _ in range(0, 10):
            start_time = time.time()
            sorter = QuickSort()
            sorted_array = sorter.sort(vector)
            end_time = time.time()
            execution_time = end_time - start_time
            self.timeExecution.append(execution_time)
        average = sum(self.timeExecution) / len(self.timeExecution)
        print("Average execution time:", average)

    def aleatoryVector(self):
        aleatoryVector = [random.randint(1, 100) for _ in range(10000)]
        self.quickSortExecution(aleatoryVector)

    def orderedVector(self):
        ordered_vector = list(range(0, 10000))
        self.quickSortExecution(ordered_vector)

comparison = QuicksortComparison()
print("Aleatory Vector")
comparison.aleatoryVector()
print("Ordered Vector")
comparison.orderedVector()
