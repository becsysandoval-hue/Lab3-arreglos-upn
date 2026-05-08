print("Etapa 4b: Ordenamiento por seleccion.")
import copy

lista_original = [64, 34, 25, 12, 22, 11, 90]
seleccion = copy.copy(lista_original)

print(f'Lista antes   (Seleccion): {seleccion}')

n = len(seleccion)

for i in range(n):
    min_idx = i

    for j in range(i + 1, n):
        if seleccion[j] < seleccion[min_idx]:
            min_idx = j

    seleccion[i], seleccion[min_idx] = seleccion[min_idx], seleccion[i]

print(f'Lista despues (Seleccion): {seleccion}')
print('\n-> Ambos algoritmos producen el mismo resultado ordenado.')
