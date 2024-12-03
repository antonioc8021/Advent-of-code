from list import Lista


class km_totales(Lista):
    for clave, valor in zip(Lista.clave, Lista.valor):
        Lista.total += abs(clave - valor)

    print(Lista.total)
