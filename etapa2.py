print('=== Ingreso de datos para la matriz 3x3 ===')
matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f'Elemento [{i}][{j}]: '))
        fila.append(valor)
    matriz.append(fila)

print('\n=== Matriz ingresada ===')
for fila in matriz:
    print(fila)

suma = 0
for fila in matriz:
    for elem in fila:
        suma += elem

print(f'\nSuma total de todos los elementos: {suma}')