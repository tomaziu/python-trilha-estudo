# EXERCÍCIO: Verificar se é Par ou Ímpar
# Objetivo: Aprender a criar e usar funções

# PASSO 1: Criar a função
# def = define uma função
# O que está entre parênteses é o parâmetro (dado que recebe)
def eh_par(num):
    # return devolve o resultado
    # num % 2 == 0 significa "o resto da divisão por 2 é 0"
    # Se for 0, é par (True). Se não, é ímpar (False)
    return num % 2 == 0

# PASSO 2: Usar a função
# Chamamos a função colocando o valor entre parênteses
print(eh_par(2))    # True (2 é par)
print(eh_par(7))    # False (7 é ímpar)
print(eh_par(10))   # True (10 é par)
print(eh_par(15))   # False (15 é ímpar)

# COMO FUNCIONA:
# eh_par(2) → 2 % 2 == 0 → 0 == 0 → True
# eh_par(7) → 7 % 2 == 0 → 1 == 0 → False
# eh_par(10) → 10 % 2 == 0 → 0 == 0 → True

# OUTRA FORMA (sem função):
# numero = 7
# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Ímpar")
# A função deixa o código reutilizável!
