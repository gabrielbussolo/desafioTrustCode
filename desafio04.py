"""
Quarto desafio

Neste problema você deve ler um conjunto de palavras, onde cada palavra é composta somente por letras no intervalo a-z e A-Z. 
Cada letra possui um valor específico, a letra a vale 1, a letra b vale 2 e assim por diante, até a letra z, que vale 26. 
Do mesmo modo, a letra A vale 27, a letra B vale 28 e a letra Z vale 52.

Você deve escrever um programa para determinar se uma palavra é uma palavra prima ou não. Uma palavra é uma palavra prima se a soma de suas letras é um número primo.
"""
import string

listaCaracteres = list(string.ascii_letters)

palavra = input("Informe a palavra: ")

contador = 0
numeros = []

#desafio 02
for cadaLetra in listaCaracteres:
    if cadaLetra in palavra:
        print(cadaLetra)
        numeros.append(contador+1)
    contador += 1

print(contador, sum(numeros))
total = sum(numeros)

#desafio 03
if total > 1:
   for i in range(2,total):
       if (total % i) == 0:
           print(f"não é primo: {total}")
           break
   else:
       print(f"é primo: {total}")
else:
   print(f"não é primo: {total}")