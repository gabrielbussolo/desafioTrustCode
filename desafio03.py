"""
Terceiro desafio

Sua tarefa agora é dado um número qualquer imprimir todos os números primos até o número dado.

Números primos são os números naturais que têm apenas dois divisores diferentes: o 1 e ele mesmo. 
Exemplos: 
1) 2 tem apenas os divisores 1 e 2, portanto 2 é um número primo. 
2) 17 tem apenas os divisores 1 e 17, portanto 17 é um número primo.
"""
numero = int(input("Informe o numero: "))

for cadaNumero in range(0, numero+1):
    if cadaNumero > 1:
        for a in range(2, cadaNumero):
            if cadaNumero % a == 0:
                break
        else:
            print(cadaNumero)