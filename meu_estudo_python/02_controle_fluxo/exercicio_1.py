while True:        
    try:
        num = int(input("Digite um número: "))
    except (ValueError, NameError):
        print("Por favor, digite um número válido.")
    else:
        if num % 2 == 0:
            print(f'O número {num} é par.')
        else:
            print(f'O número {num} é ímpar.')
    
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break