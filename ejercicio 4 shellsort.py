"""
Ordenamiento ShellSort
Menú que pide la cantidad de números y los números, los ordena con
ShellSort y repite hasta que el usuario decida salir.
"""


def shell_sort(lista):
    """Ordena una lista de enteros con ShellSort (secuencia de Shell: n/2, n/4, ... 1)."""
    arr = lista.copy()          # no modificamos la lista original
    n = len(arr)
    salto = n // 2              # distancia inicial entre elementos a comparar

    while salto > 0:
        # Insertion sort sobre los elementos separados por 'salto'
        for i in range(salto, n):
            temp = arr[i]
            j = i
            while j >= salto and arr[j - salto] > temp:
                arr[j] = arr[j - salto]
                j -= salto
            arr[j] = temp
        salto //= 2             # reducimos el salto a la mitad
    return arr


def pedir_entero(mensaje, minimo=None):
    """Pide un entero por teclado y repite hasta que sea válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  Debe ser un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida, escribe un número entero.")


def pedir_numeros():
    """Pide la cantidad de números y luego cada número."""
    cantidad = pedir_entero("¿Cuántos números deseas ordenar? ", minimo=1)
    numeros = []
    for i in range(cantidad):
        numeros.append(pedir_entero(f"  Número {i + 1}: "))
    return numeros


def menu():
    print("\n===== ORDENAMIENTO SHELLSORT =====")
    print("1. Ordenar números")
    print("2. Salir")


def main():
    while True:
        menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            numeros = pedir_numeros()
            print("\nLista original :", numeros)
            print("Lista ordenada :", shell_sort(numeros))
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()