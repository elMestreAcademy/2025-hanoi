# Torres de Hanoi

El juego de las Torres de Hanoi consiste en mover una serie de discos de distintos tamaños entre tres torres. El objetivo es trasladar todos los discos desde la torre de origen a la torre destino, utilizando una torre auxiliar, pero siempre respetando las siguientes reglas:

**Un solo disco a la vez**: Solo se puede mover el disco que está en la parte superior de una torre.

**Movimiento individual**: Cada movimiento implica tomar el disco superior de una torre y colocarlo en la parte superior de otra.

**Orden creciente**: Nunca se puede colocar un disco grande encima de un disco más pequeño.

La solución ideal se basa en un enfoque recursivo, donde se resuelve el problema dividiéndolo en subproblemas más pequeños.

## Reglas del juego

- El objetivo es llevar todos los discos a una misma varilla
- Mover los discos de uno en uno
- No se puede poner un disco más grande sobre otro más pequeño

## Desarrollo del juego

- Colocar los discos en una varilla, de mayor a menor tamaño
- Mover un disco de una varilla a otra
- Repetir el paso 2 hasta que todos los discos estén en la misma varilla
