# EXERCÍCIO 3: Calculadora com Input
# Objetivo: Aprender a pedir dados ao usuário

# PASSO 1: Pedir o primeiro número
# input() mostra uma mensagem e espera o usuário digitar
# int() converte o texto digitado para número inteiro
num1 = int(input("Digite o primeiro número: "))

# PASSO 2: Pedir o segundo número
num2 = int(input("Digite o segundo número: "))

# PASSO 3: Mostrar os resultados
print(f'A soma de {num1} e {num2} é: {num1 + num2}')
print(f'A subtração de {num1} e {num2} é: {num1 - num2}')
print(f'A multiplicação de {num1} e {num2} é: {num1 * num2}')

# COMO FUNCIONA:
# 1. O programa mostra "Digite o primeiro número: "
# 2. O usuário digita algo (ex: 10)
# 3. O input() retorna "10" (texto)
# 4. O int() converte "10" para 10 (número)
# 5. Agora podemos fazer contas com num1

# POR QUE USAR int()?
# O input() sempre retorna TEXTO
# Se não converter, "10" + "5" = "105" (junta textos)
# Com int(), 10 + 5 = 15 (faz a soma)
