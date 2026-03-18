import os
os.system('cls')

#----- Desafio 003 - Crie um programa que leia dois números e  mostre a soma entre eles.

print('======== SOMANDO DOIS NÚMEROS ========')

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = n1 + n2

print(f'\nA soma entre {n1} e {n2} é -> {soma}')