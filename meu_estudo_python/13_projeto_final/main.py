# PROJETO FINAL: Gerenciador de Contatos
# Conceitos: POO, arquivos CSV, validação, strings

import csv
import os
from contato import Contato

# Nome do arquivo onde os contatos serão salvos
ARQUIVO_CSV = "contatos.csv"

def carregar_contatos() -> list[Contato]:
    """Carrega contatos do arquivo CSV"""
    contatos = []
    
    # Verifica se o arquivo existe antes de ler
    if os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, "r", encoding="utf-8") as arquivo:
            # DictReader lê cada linha como dicionário
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                contatos.append(Contato.from_dict(linha))
    
    return contatos

def salvar_contatos(contatos: list[Contato]) -> None:
    """Salva todos os contatos no arquivo"""
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "telefone", "email", "cidade"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()  # Cabeçalho: nome,telefone,email,cidade
        
        for contato in contatos:
            escritor.writerow(contato.to_dict())
    
    print(f"✓ {len(contatos)} contatos salvos!")

def cadastrar_contato(contatos: list[Contato]) -> None:
    """Cadastra um contato novo"""
    print("\n═══ Novo Contato ═══")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cidade = input("Cidade: ")
    
    # Cria objeto Contato
    contato = Contato(nome, telefone, email, cidade)
    contatos.append(contato)
    print(f"✓ {contato.nome} cadastrado!")

def listar_contatos(contatos: list[Contato]) -> None:
    """Lista todos os contatos"""
    if not contatos:
        print("✗ Nenhum contato cadastrado.")
        return
    
    print("\n═══ Todos os Contatos ═══")
    for i, contato in enumerate(contatos, 1):
        print(f"{i}. {contato}")

def buscar_contato(contatos: list[Contato]) -> None:
    """Busca contato por nome (parcial)"""
    termo = input("Digite o nome para buscar: ").strip().lower()
    
    # Filtra: mantém contatos onde o termo está no nome
    resultados = [c for c in contatos if termo in c.nome.lower()]
    
    if not resultados:
        print(f"✗ Nenhum contato com '{termo}'.")
        return
    
    print(f"\n═══ Resultados para '{termo}' ═══")
    for contato in resultados:
        print(f"  {contato}")

def filtrar_por_cidade(contatos: list[Contato]) -> None:
    """Filtra contatos por cidade"""
    cidade = input("Digite a cidade: ").strip().title()
    resultados = [c for c in contatos if c.cidade == cidade]
    
    if not resultados:
        print(f"✗ Nenhum contato em {cidade}.")
        return
    
    print(f"\n═══ Contatos em {cidade} ═══")
    for contato in resultados:
        print(f"  {contato}")

def estatisticas(contatos: list[Contato]) -> None:
    """Mostra estatísticas dos contatos"""
    if not contatos:
        print("✗ Nenhum contato cadastrado.")
        return
    
    # Conta contatos por cidade
    cidades = {}
    for contato in contatos:
        cidades[contato.cidade] = cidades.get(contato.cidade, 0) + 1
    
    print("\n═══ Estatísticas ═══")
    print(f"Total de contatos: {len(contatos)}")
    print("\nPor cidade:")
    for cidade, total in sorted(cidades.items()):
        print(f"  {cidade}: {total}")

def menu() -> None:
    """Menu principal"""
    contatos = carregar_contatos()
    print(f"Carregados {len(contatos)} contatos.\n")
    
    while True:
        print("\n╔═══════════════════════════════╗")
        print("║   GERENCIADOR DE CONTATOS     ║")
        print("╠═══════════════════════════════╣")
        print("║  1. Cadastrar contato         ║")
        print("║  2. Listar contatos           ║")
        print("║  3. Buscar por nome           ║")
        print("║  4. Filtrar por cidade        ║")
        print("║  5. Ver estatísticas          ║")
        print("║  6. Salvar e sair             ║")
        print("╚═══════════════════════════════╝")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            cadastrar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            buscar_contato(contatos)
        elif opcao == "4":
            filtrar_por_cidade(contatos)
        elif opcao == "5":
            estatisticas(contatos)
        elif opcao == "6":
            salvar_contatos(contatos)
            print("Até mais!")
            break
        else:
            print("✗ Opção inválida.")

if __name__ == "__main__":
    menu()
