class MergeSort:
    def sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Encontra o ponto médio do vetor
            left_half = arr[:mid]  # Divide o vetor em duas metades
            right_half = arr[mid:]

            self.sort(left_half)  # Ordena a metade esquerda
            self.sort(right_half)  # Ordena a metade direita

            i = j = k = 0

            # Combina as duas metades ordenadas
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr  # Return the sorted array directly