# EXERCÍCIO: Cadastro de Alunos com Arquivo
# Objetivo: Aprender manipulação de arquivos e dicionários

# Lista para guardar todos os cadastros
alunos = []

def cadastrar_aluno():
    """Cadastra um aluno novo"""
    print("\n═══ Novo Aluno ═══")
    nome = input("Nome: ")
    
    # Pedir 3 notas com validação
    while True:
        try:
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
            break
        except ValueError:
            print("✗ Digite um número válido.")
    
    # Calcular média
    media = (nota1 + nota2 + nota3) / 3
    
    # Criar dicionário com os dados
    # Dicionário guarda dados com CHAVE: VALOR
    aluno = {
        "nome": nome,
        "notas": [nota1, nota2, nota3],
        "media": media
    }
    
    # Adicionar na lista de alunos
    alunos.append(aluno)
    print(f"✓ Aluno {nome} cadastrado com sucesso!")

def salvar_em_arquivo():
    """Salva todos os cadastros no arquivo"""
    # 'w' = write (apaga e reescreve)
    with open("alunos_cadastrados.txt", "w") as arquivo:
        for aluno in alunos:
            arquivo.write(f"═══════════════════════════\n")
            arquivo.write(f"Nome: {aluno['nome']}\n")
            arquivo.write(f"Notas: {aluno['notas']}\n")
            arquivo.write(f"Média: {aluno['media']:.2f}\n")
    print(f"✓ {len(alunos)} alunos salvos em 'alunos_cadastrados.txt'")

def listar_alunos():
    """Mostra todos os cadastrados"""
    if not alunos:  # Se a lista está vazia
        print("✗ Nenhum aluno cadastrado ainda.")
        return
    
    print("\n═══ Lista de Alunos ═══")
    # enumerate() retorna posição e valor
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. {aluno['nome']} - Média: {aluno['media']:.2f}")

# MENU PRINCIPAL
while True:
    print("\n╔═══════════════════════════╗")
    print("║   SISTEMA DE CADASTRO     ║")
    print("╠═══════════════════════════╣")
    print("║  1. Cadastrar aluno       ║")
    print("║  2. Listar alunos         ║")
    print("║  3. Salvar e sair         ║")
    print("╚═══════════════════════════╝")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        if alunos:
            salvar_em_arquivo()
        else:
            print("✗ Nada para salvar.")
        print("Até mais!")
        break
    else:
        print("✗ Opção inválida.")

# COMO FUNCIONA O DICIONÁRIO:
# aluno = {"nome": "Ana", "notas": [8, 7, 9], "media": 8.0}
# aluno["nome"] → "Ana"
# aluno["notas"] → [8, 7, 9]
# aluno["media"] → 8.0
