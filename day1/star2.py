from list import Lista


class numeros_repetidos(Lista):
    # inicializo un contador de veces que se repiten los números
    # inicializo un sumatorio de todos los números que se repiten
    contador_numeros_repetidos = 0
    sumatorio = 0
    for clave in Lista.clave:
        for valor in Lista.valor:
            if clave == valor:
                contador_numeros_repetidos += 1
        sumatorio += clave * contador_numeros_repetidos
        print(contador_numeros_repetidos)
        # restablezco el valor a 0 para que no se sume el contador al valor anterior
        contador_numeros_repetidos = 0
    print(sumatorio)
