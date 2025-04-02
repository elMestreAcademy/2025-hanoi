model = [[1, 2, 3, 4], [], []]


def hanoi(cantidad, origen, destino, aux):
    global model
    if cantidad == 1:
        print(f"Mueve disco de {origen} a {destino}")
        print(model)
        model[destino].append(model[origen].pop())
    else:
        hanoi(cantidad - 1, origen, aux, destino)
        hanoi(1, origen, destino, aux)
        hanoi(cantidad - 1, aux, destino, origen)


hanoi(4, 0, 2, 1)  # mueve del palo 0 al 2 usindo el 1 como aux
