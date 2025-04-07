def construir_adyacencias():
  
    return {
        '0': ['0','8'],
        '1': ['1','2','4'],
        '2': ['1','2','3','5'],
        '3': ['2','3','6'],
        '4': ['1','4','5','7'],
        '5': ['2','4','5','6','8'],
        '6': ['3','5','6','9'],
        '7': ['4','7','8'],
        '8': ['5','7','8','9','0'],
        '9': ['6','8','9']
    }

def contar_secuencias(digito, largo, memo, adyacencias):

    if largo == 1:
        return 1

    if (digito, largo) in memo:
        return memo[(digito, largo)]

    total = 0
    for vecino in adyacencias[digito]:
        total += contar_secuencias(vecino, largo - 1, memo, adyacencias)

    memo[(digito, largo)] = total
    return total

def contar_todas_secuencias(n):

    adyacencias = construir_adyacencias()
    memo = {}
    total_final = 0

    # Se suma para cada dígito inicial (0..9)
    for d in ['0','1','2','3','4','5','6','7','8','9']:
        total_final += contar_secuencias(d, n, memo, adyacencias)

    return total_final

resultado_n10 = contar_todas_secuencias(10)
print("La cantidad de combinaciones posibles para n=10 es:", resultado_n10)

