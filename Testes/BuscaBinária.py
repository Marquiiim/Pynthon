# Fazer um algoritmo de busca linear e busca binária em Python para ordenar uma lista.

vetor = [48, 12, 5, 34, 23, 79, 56, 3, 91, 27]

def bubble_sort(lista):
    n = len(lista)
    for i in range (n - 1):
        for j in range (n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

bubble_sort(vetor)

def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

print(busca_binaria(vetor, 23))

# OUTRO TESTE

vetor = [42, 17, 23, 8, 34, 54, 3, 29, 11]

def bubble_sort(lista):
    n = len(lista)
    for i in range (n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

bubble_sort(vetor)

def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

print(busca_binaria(vetor, 17))