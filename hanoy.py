# Source: https://www.openbookproject.net/py4fun/hanoi/hanoi.html

import view

model = [[1, 2, 3, 4], [], []]


def hanoi(ndiscs, src, dest, aux):
    global model
    if ndiscs == 1:
        print("move disc from %s to %s" % (src, dest))
        print(model)
        view.moveDisc(model, src, dest)  # send signal to view code
        model[dest].append(model[src].pop())  # move disc from src to dest
    else:
        hanoi(ndiscs - 1, src, aux, dest)
        hanoi(1, src, dest, aux)
        hanoi(ndiscs - 1, aux, dest, src)


def main(ndiscs):
    global draw
    view.init(model)  # ask view code to set up visualization
    model[0] = list(range(1, ndiscs + 1))
    hanoi(ndiscs, 0, 2, 1)  # move stack on peg 0 to peg 2 using peg 1 as auxiallary


main(4)
