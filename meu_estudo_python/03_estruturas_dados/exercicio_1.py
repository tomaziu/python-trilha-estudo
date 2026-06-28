nomes = []

for i in range(1, 6):
    nome = input(f"Digite o nome da pessoa {i}: ")
    nomes.append(nome)


while True:
    print("Pesquisar um nome na lista:")
    nome_pesquisado = input("Digite o nome que deseja pesquisar: ").strip()

    if nome_pesquisado in nomes:
        print(f"O nome '{nome_pesquisado}' foi encontrado na lista.")
    else:
        print(f"O nome '{nome_pesquisado}' não foi encontrado na lista.")   
    continuar = input("Deseja pesquisar outro nome? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break

unicos = set(nomes)

print(f"\nNomes únicos na lista: {len(unicos)}")