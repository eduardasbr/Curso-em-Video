import os
os.system('cls')

#----- Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('=' * 40)
print('          ANÁLISE DO CARACTERE')
print('=' * 40)

n = input('\nDigite algo: ')

print(f'É numérico? -> {n.isnumeric()}')
print(f'É alfabético? -> {n.isalpha()}')
print(f'É alfanumérico? -> {n.isalnum()}')
print(f'É maiúsculo? -> {n.isupper()}')
print(f'É minúsculo? -> {n.islower()}')
print(f'É espaço? -> {n.isspace()}')
print(f'É capitalizada? -> {n.istitle()}')




