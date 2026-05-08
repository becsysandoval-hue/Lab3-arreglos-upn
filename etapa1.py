# ─── Etapa 1: Listas unidimensionales ─────────────────────────────

lista = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Lista original:")
for elemento in lista:
    print(elemento)

nuevo_valor = int(input("\nIngrese un nuevo valor para reemplazar el tercer elemento: "))
lista[2] = nuevo_valor

print("\nLista modificada:")
for elemento in lista:
    print(elemento)

buscar = int(input("\nIngrese un número para buscar en la lista: "))

if buscar in lista:
    print(f"El número {buscar} sí existe en la lista.")
else:
    print(f"El número {buscar} no existe en la lista.")