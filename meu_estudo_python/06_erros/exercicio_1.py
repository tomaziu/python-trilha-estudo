while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Por favor, digite um número válido.")

while True:
    print('''
Escolha a operação desejada:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
''')
    try:
        operacao = int(input("Digite o número da operação desejada (1/2/3/4): "))
    except (ValueError, NameError):
        print("Por favor, digite um número válido.")
    
    try:
        if operacao == 1:
            resultado = num1 + num2
            print(f"O resultado da adição é: {resultado}")
            break
        elif operacao == 2:
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
            break
        elif operacao == 3:
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
            break
        elif operacao == 4:
            try:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}")
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
                break
        else:
            print("Operação inválida. Por favor, escolha uma operação entre 1 e 4.")
    except:
        pass