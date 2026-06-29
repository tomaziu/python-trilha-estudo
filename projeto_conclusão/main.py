import contato
import re
import pandas as pd
import os

def cadastro_nome():
    while True:
        nome = input("Digite seu nome: ")
        if all(palavra.isalpha() for palavra in nome.split()):
            return nome
        else:
            print("Nome inválido, tente novamente")

def cadastro_telefone():
    while True:
        try:
            telefone = int(input("Digite o número de telefone: "))
            return telefone

        except ValueError:
            print("Número incorreto, tente novamente")

def cadastro_email():
    
    while True:
        email = input("Digite seu email: ").strip()

        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if re.match(padrao, email):
            return email
        else:
            print("Email inválido, tente novamente")

def cadastrar_cidade():
    while True:
        cidade = input("Digite sua cidade: ")
        if all(palavra.isalpha() for palavra in cidade.split()):
            return cidade
        else:
            print("Cidade inválida, tente novamente")

while True:
    cadastrar = True
    
    print("~~~~~~~~~~~~~~ [ PAINEL ADMIN ] ~~~~~~~~~~~~~~")
    print("[ 1 ] Cadastrar")
    print("[ 2 ] Listar")
    print("[ 3 ] Buscar")
    print("[ 4 ] Filtrar (por cidade)")
    print("[ 5 ] Estatísticas")
    print("[ 0 ] Sair")
    escolha = input("R. ")

    if escolha == "1":
        while cadastrar:
            print("~~~~~~~~~~~~~~ [ CADASTRO ] ~~~~~~~~~~~~~~")
            
            nome = cadastro_nome()
            telefone = cadastro_telefone()
            email = cadastro_email()
            cidade = cadastrar_cidade()

            contatos = [contato.Contato(nome, telefone, email, cidade)]

            header = not os.path.exists('contatos.csv') or os.path.getsize('contatos.csv') == 0
            df = pd.DataFrame([vars(c) for c in contatos])
            df.to_csv('contatos.csv', mode='a', header=header, index=False)

            while True:
                print("Deseja cadastrar mais usuários?\n[ 1 ] Sim\n[ 2 ] Não")
                parada = input("R. ")

                if parada == "1":
                    break
                elif parada == "2":
                    cadastrar = False
                    break
                else:
                    print("Alternativa incorreta")
    elif escolha == "2":
        if os.path.exists('contatos.csv'):
            df = pd.read_csv('contatos.csv')
            for _, row in df.iterrows():
                c = contato.Contato(row['nome'], row['telefone'], row['email'], row['cidade'])
                print(c)
                print()
        else:
            print("Nenhum contato cadastrado ainda.")     
    elif escolha == "3":
        if os.path.exists('contatos.csv'):
            busca = input("Digite o nome: ")
            df = pd.read_csv('contatos.csv')
            resultado = df[df['nome'].str.contains(busca, case=False)]
            
            if resultado.empty:
                print("Contato não encontrado.")
            else:
                for _, row in resultado.iterrows():
                    c = contato.Contato(row['nome'], row['telefone'], row['email'], row['cidade'])
                    print(c)
                    print()
        else:
            print("Nenhum contato cadastrado ainda.")     
    elif escolha == "4":
        if os.path.exists('contatos.csv'):
            cidade = input("Digite a cidade: ")
            df = pd.read_csv('contatos.csv')
            resultado = df[df['cidade'].str.lower() == cidade.lower()]
            
            if resultado.empty:
                print("Nenhum contato nessa cidade.")
            else:
                for _, row in resultado.iterrows():
                    c = contato.Contato(row['nome'], row['telefone'], row['email'], row['cidade'])
                    print(c)
                    print()
        else:
            print("Nenhum contato cadastrado ainda.")
    elif escolha == "5":
        if os.path.exists('contatos.csv'):
            df = pd.read_csv('contatos.csv')
            stats = df['cidade'].value_counts().reset_index()
            stats.columns = ['Cidade', 'Total']
            print(stats.to_string(index=False))
        else:
            print("Nenhum contato cadastrado ainda.")
    elif escolha == "0":
        print("Encerrando programa...")
        exit()
    else:
        print("Alternativa incorreta!")
