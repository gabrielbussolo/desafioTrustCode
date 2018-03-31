"""
Primeiro desafio

Você recebe uma lista de 300 números ordenados por ordem crescente.
Sua tarefa é achar um número aleatório informado pelo usuário da maneira mais eficiente possível.
"""
from random import randint

lista = sorted([randint(0, 5000000) for x in range(300)])
numero = int(input("Informe um número: "))
if numero in lista:
    print("Número encontrado.")
else:
    print("Número não encontrado.")
