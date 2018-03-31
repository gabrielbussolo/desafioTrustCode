"""
Segundo desafio

Agora sua lista de 500 números não estão ordenados.
>>lista = [randint(0, 5000000) for x in range(500)]

E você recebe uma outra lista com 50000 números também aleatórios.
>>lista = [randint(0, 5000000) for x in range(50000)]

Sua tarefa é para cada item da segunda lista, imprimir quais destes números estão na primeira lista recebido.
Pontos para a solução mais rápida.
"""
from random import randint

lista1 = [randint(0, 5000000) for x in range(500)]
lista2 = [randint(0, 5000000) for x in range(50000)]

for cadaNumero in lista2:
    if cadaNumero in lista1:
        print (cadaNumero)