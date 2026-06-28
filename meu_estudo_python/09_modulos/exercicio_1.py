from random import choice
from math import sqrt

def num(escolhas):
    return choice(escolhas)

lista_numeros = []
for i in range(3):
    usuario_escolha = input("Escolha um número: ")
    lista_numeros.append(usuario_escolha)

num1 = num(lista_numeros)

print(f"Os números escolhidos foram: {', '.join(lista_numeros)}")
print(f"Você escolheu: {num1}")

print(f"A raiz quadrada do número escolhido é: {sqrt(int(num1)):.2f}")
