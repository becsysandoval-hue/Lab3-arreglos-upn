
import copy


lista_original = [64, 34, 25, 12, 22, 11, 90]
burbuja = copy.copy(lista_original)


print(f'Lista antes  (Burbuja): {burbuja}')


n = len(burbuja)
for i in range(n - 1):
    for j in range(n - i - 1):
        if burbuja[j] > burbuja[j + 1]:
            burbuja[j], burbuja[j + 1] = burbuja[j + 1], burbuja[j]


print(f'Lista despues (Burbuja): {burbuja}')
