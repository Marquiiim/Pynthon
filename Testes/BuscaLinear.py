# Fazer um algoritmo de busca linear e busca binária em Python para ordenar uma lista.

vetor = [42, 17, 23, 8, 34, 54, 3, 29, 11]

def busca_linear(lista, elemento):
    for i in range (len(lista)):
        if lista[i] == elemento:
            return i
    return -1

print(busca_linear(vetor, 54))

# OUTRO TESTE

vetor = [3.14, -7.5, 0, 42, -1.2, 8.8, 23, -11, 5.5]

def busca_linear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

print(busca_linear(vetor, 3.14))