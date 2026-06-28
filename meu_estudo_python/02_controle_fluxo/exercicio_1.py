# EXERCÍCIO: Tabuada com Loop
# Objetivo: Aprender laços de repetição (while e for)

# PASSO 1: Criar um loop que continua até o usuário querer parar
while True:  # True = sempre verdadeiro (loop infinito até dar break)
    
    # PASSO 2: Pedir um número ao usuário
    # try/except trata erros (se digitar letra em vez de número)
    try:
        num = int(input("Digite um número: "))
    except (ValueError, NameError):
        # Se deu erro, mostra mensagem e volta ao início do while
        print("Por favor, digite um número válido.")
    else:
        # Se NÃO deu erro, executa este bloco
        # Verificar se é par ou ímpar
        # % = módulo (resto da divisão)
        # Se resto == 0, é par
        if num % 2 == 0:
            print(f'O número {num} é par.')
        else:
            print(f'O número {num} é ímpar.')
    
    # PASSO 3: Mostrar a tabuada
    # range(1, 11) gera números de 1 até 10
    # for repete algo para cada número
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

    # PASSO 4: Perguntar se quer continuar
    continuar = input("Deseja continuar? (s/n): ")
    # .strip() remove espaços extras
    # .lower() converte para minúsculo
    continuar = continuar.strip().lower()
    
    # Se digitou algo diferente de 's', sai do loop
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break  # break sai do loop while

# COMO FUNCIONA O LOOP:
# 1. Enquanto True for verdadeiro, o código repete
# 2. A cada volta, pede número e mostra tabuada
# 3. Se usuário digitar 'n' (ou qualquer coisa ≠ 's'), break para o loop
