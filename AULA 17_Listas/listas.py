import os
os.system('cls')

lanches = ['hamburguer', 'pizza', 'pudim', 'refrigerante']

print(f'Sua lista: {lanches}')

# Remover um elemento - Pedido do usuário

removElem = input(print('Digite o elemento que deseja remover: '))

if removElem in lanches:
    lanches.remove(removElem)
    print(f'Elemento {removElem} removido.')
    print(f'Sua lita agora é: {lanches}')
else:
    print('Elemento não localizado')


# Adicionar um elemento - Pedido do Usuário

addElem = input(print('Insira o Elemento que deseja adicionar: '))

lanches.append(addElem)

print(f'Sua lista agora é: {lanches}')

