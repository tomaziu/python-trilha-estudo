# EXERCÍCIO: Calculadora com Validação
# Objetivo: Aprender try/except para tratar erros

# PASSO 1: Pedir números com validação
while True:
    # try tenta executar o código
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        break  # Se não deu erro, sai do loop
    except ValueError:
        # ValueError = erro quando não converte para número
        # Exemplo: int("abc") → erro!
        print("✗ Por favor, digite apenas números inteiros.")

# PASSO 2: Mostrar menu de operações
while True:
    print('''
    ╔══════════════════════════════╗
    ║     ESCOLHA A OPERAÇÃO       ║
    ╠══════════════════════════════╣
    ║  1. Adição (+)               ║
    ║  2. Subtração (-)            ║
    ║  3. Multiplicação (x)        ║
    ║  4. Divisão (/)              ║
    ╚══════════════════════════════╝
    ''')
    
    try:
        operacao = int(input("Digite o número da operação: "))
    except ValueError:
        print("✗ Digite um número de 1 a 4.")
        continue  # Volta ao início do loop
    
    # PASSO 3: Executar a operação escolhida
    try:
        if operacao == 1:
            resultado = num1 + num2
            print(f"\n✓ {num1} + {num2} = {resultado}")
            break
        elif operacao == 2:
            resultado = num1 - num2
            print(f"\n✓ {num1} - {num2} = {resultado}")
            break
        elif operacao == 3:
            resultado = num1 * num2
            print(f"\n✓ {num1} x {num2} = {resultado}")
            break
        elif operacao == 4:
            try:
                resultado = num1 / num2
                print(f"\n✓ {num1} / {num2} = {resultado}")
                break
            except ZeroDivisionError:
                # ZeroDivisionError = dividir por zero
                print("✗ Erro: Não existe divisão por zero!")
        else:
            print("✗ Opção inválida. Escolha entre 1 e 4.")
    except Exception as e:
        print(f"✗ Erro inesperado: {e}")

# COMO FUNCIONA O TRY/EXCEPT:
# try: tenta rodar o código
# Se der ERRO: pula pro except
# Se NÃO der erro: ignora o except
# É como um "seguro" contra erros
