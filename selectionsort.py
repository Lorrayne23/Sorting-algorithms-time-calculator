class Selection:
    @staticmethod
    def selectionSort(array):
        for fillslot in range(len(array) - 1, 0, -1):
            print('Entrou aqui')
            positionOfMax = 0
            for location in range(1, fillslot + 1):
                if array[location] > array[positionOfMax]:
                    positionOfMax = location

            temp = array[fillslot]
            array[fillslot] = array[positionOfMax]
            array[positionOfMax] = temp

        return array  # Retorna o array ordenado



