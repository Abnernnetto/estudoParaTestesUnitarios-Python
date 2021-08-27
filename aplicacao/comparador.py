
def compara_numeros_simples(numero_a, numero_b):
    if(numero_a > numero_b):
        return True
    elif(numero_b > numero_a):
        return True
    else:
        return False


def compara_numeros_quadraplos(numero_a, numero_b, numero_x, numero_y):
    if ((numero_a > numero_b) & (numero_x < numero_y)):
        return True
    return False

compara_numeros_simples(5, 2)
compara_numeros_simples(1, 2)
compara_numeros_simples(5, 5)

compara_numeros_quadraplos(6, 5, 1, 2)
compara_numeros_quadraplos(6, 5, 3, 2)
compara_numeros_quadraplos(1, 5, 1, 2)
compara_numeros_quadraplos(1, 5, 7, 2)
compara_numeros_quadraplos(1, 1, 1, 1)
compara_numeros_quadraplos(1, 1, 2, 1)
compara_numeros_quadraplos(1, 1, 1, 2)
compara_numeros_quadraplos(1, 2, 3, 3)
compara_numeros_quadraplos(2, 1, 5, 5)

