lista = [10, 25, 38, 47, 52]

while True:
    print('\n--- MENU DE OPERACIONES ---')
    print('1. Insertar elemento al final')
    print('2. Eliminar elemento por posicion')
    print('3. Buscar un valor en la lista')
    print('4. Mostrar la lista completa')
    print('5. Salir')

    opcion = input('Selecciona una opcion: ').strip()

    if opcion == '1':
        val = int(input('Valor a insertar: '))
        lista.append(val)
        print(f'-> Elemento {val} agregado. Lista: {lista}')

    elif opcion == '2':
        pos = int(input('Posicion a eliminar (0 en adelante): '))
        if 0 <= pos < len(lista):
            eliminado = lista.pop(pos)
            print(f'-> Se elimino el valor {eliminado}. Lista: {lista}')
        else:
            print('-> Posicion invalida, intenta de nuevo.')

    elif opcion == '3':
        val = int(input('Valor a buscar: '))
        if val in lista:
            print(f'-> {val} esta en la posicion {lista.index(val)}.')
        else:
            print(f'-> {val} no se encuentra en la lista.')

    elif opcion == '4':
        print(f'-> Lista actual: {lista}')

    elif opcion == '5':
        print('Saliendo del menu. Hasta luego.')
        break

    else:
        print('-> Opcion no reconocida, intenta de nuevo.')