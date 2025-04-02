from time import sleep
import os


def mostrar_torres(torres):
    if False:
        for i, torre in enumerate(torres):
            print(f"Torre {i}: {torre}")
        print("-" * 40)
    else:
        mostrar_torres_ascii(torres)


def limpiar_pantalla():
    os.system('cls')


def mostrar_torres_ascii(torres):
    sleep(0.5)
    limpiar_pantalla()
    # Número total de discos (constante en el juego)
    total_discos = sum(len(t) for t in torres)
    ancho = 2 * total_discos - 1  # Ancho máximo de un disco (disco más grande)
    altura = total_discos         # Número de niveles a mostrar

    # Construimos una representación en ASCII para cada torre
    torres_display = []
    for torre in torres:
        niveles = []
        # Calcula los niveles vacíos (cuando la torre no tiene disco en ese nivel)
        niveles_vacios = altura - len(torre)
        # Añadimos los niveles vacíos (se usa "|" centrado)
        for _ in range(niveles_vacios):
            niveles.append("|".center(ancho))
        # Los discos de la torre: el tope es el último elemento de la lista.
        # Los mostramos de arriba a abajo (por eso se recorre en orden inverso).
        for disco in reversed(torre):
            # El disco se representa con 2*d - 1 caracteres "="
            disco_repr = ("=" * (2 * disco - 1)).center(ancho)
            niveles.append(disco_repr)
        torres_display.append(niveles)

    # Imprimimos línea a línea (de arriba hacia abajo)
    for nivel in range(altura):
        linea = "   ".join(torres_display[i][nivel] for i in range(len(torres)))
        print(linea)

    # Imprimir una base y los índices de las torres
    base = "   ".join("-" * ancho for _ in range(len(torres)))
    print(base)
    indices = "   ".join(str(i).center(ancho) for i in range(len(torres)))
    print(indices)


def mover(n, torres, origen, destino, aux):
    # Caso base: mover un solo disco.
    if n == 1:
        disco = torres[origen].pop()
        torres[destino].append(disco)
        print(f"Moviendo disco {disco} de torre {origen} a torre {destino}")
        mostrar_torres(torres)
    else:
        # Mover n-1 discos de origen a auxiliar.
        mover(n - 1, torres, origen, aux, destino)
        # Mover el disco restante de origen a destino.
        mover(1, torres, origen, destino, aux)
        # Mover los n-1 discos que dejamos en auxiliar a destino.
        mover(n - 1, torres, aux, destino, origen)


def hanoi(n):
    # Inicializamos 0 con n discos y las demás vacías.
    torres = [list(range(n, 0, -1)), [], []]

    print("Estado inicial:")
    mostrar_torres(torres)

    # Llamamos a la función recursiva pasando n como número de discos a mover.
    mover(n, torres, origen=0, destino=2, aux=1)

    print("Estado final:")
    mostrar_torres(torres)


hanoi(6)
