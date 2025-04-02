def hanoi(modelo, cantidad, origen, destino, aux):
    if cantidad == 1:
        print(f"Mueve disco de {origen} a {destino}")
        print(modelo)
        modelo[destino].append(modelo[origen].pop())
    else:
        hanoi(modelo, cantidad - 1, origen, aux, destino)
        hanoi(modelo, 1, origen, destino, aux)
        hanoi(modelo, cantidad - 1, aux, destino, origen)


modelo = [[1, 2, 3, 4], [], []]
hanoi(modelo, 4, 0, 2, 1)  # mueve del palo 0 al 2 usindo el 1 como aux
