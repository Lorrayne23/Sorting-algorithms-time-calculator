import random

# Criar 50 vetores que devem ser aleatoriamente preenchidos com cada tamanho do vetor está na lista

vectorSizes = [62500, 125000, 250000, 375000]

for size in vectorSizes:

    for _ in range(50):
        print(str(size))
        aleatoryVector = [random.randint(1, 100) for _ in range(size)]
        #print(aleatoryVector)
        print("----------------------------------------")

