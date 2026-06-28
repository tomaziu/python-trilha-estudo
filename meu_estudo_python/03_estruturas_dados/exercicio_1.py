# EXERCÍCIO: Agenda de Contatos
# Objetivo: Aprender listas, busca e sets

# PASSO 1: Criar lista vazia
# Lista é uma coleção ordenada de itens
nomes = []

# PASSO 2: Coletar 5 nomes do usuário
# range(1, 6) gera: 1, 2, 3, 4, 5
for i in range(1, 6):
    nome = input(f"Digite o nome da pessoa {i}: ")
    nomes.append(nome)  # append() adiciona no final da lista

# PASSO 3: Criar loop de busca
while True:
    print("\n--- Pesquisar nome na lista ---")
    nome_pesquisado = input("Digite o nome para pesquisar: ").strip()

    # 'in' verifica se o item existe na lista
    # Retorna True ou False
    if nome_pesquisado in nomes:
        print(f"✓ O nome '{nome_pesquisado}' FOI encontrado na lista.")
    else:
        print(f"✗ O nome '{nome_pesquisado}' NÃO foi encontrado na lista.")   
    
    # Perguntar se quer continuar
    continuar = input("Pesquisar outro nome? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break

# PASSO 4: Contar nomes únicos
# set() remove duplicatas automaticamente
# Exemplo: ["Ana", "João", "ANA"] vira {"Ana", "João"} (tudo minúsculo no set)
unicos = set(nomes)
print(f"\nTotal de nomes: {len(nomes)}")
print(f"Nomes únicos: {len(unicos)}")

# COMO FUNCIONA A LISTA:
# nomes começa como []
# nomes.append("Ana") → ["Ana"]
# nomes.append("João") → ["Ana", "João"]
# nomes.append("Ana") → ["Ana", "João", "Ana"]
# set(nomes) → {"Ana", "João"} (remove a repetição)
