# 07 — Manipulação de Arquivos

**O que é:** Ler, escrever e modificar arquivos no computador. Isso serve para salvar dados, gerar relatórios, importar informações de CSV, entre muitas outras coisas.

## O que está incluído

| Conceito | O que faz | Exemplo |
|----------|-----------|---------|
| `open()` | Abre um arquivo | `open("dados.txt", "r")` |
| `read()` | Lê todo o conteúdo | `arquivo.read()` |
| `write()` | Escreve no arquivo | `arquivo.write("texto")` |
| `with open` | Abre e fecha automaticamente | Mais seguro e recomendado |
| Modo `r` | Leitura (padrão) | `open("arq.txt", "r")` |
| Modo `w` | Escrita (apaga o que já tem) | `open("arq.txt", "w")` |
| Modo `a` | Adiciona no final (não apaga) | `open("arq.txt", "a")` |

## Como funciona na prática

```python
# ESCREVER em um arquivo
with open("contatos.txt", "w") as arquivo:
    arquivo.write("Ana - 99999-1234\n")
    arquivo.write("João - 88888-5678\n")

# LER um arquivo
with open("contatos.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# ADICIONAR no final (sem apagar)
with open("contatos.txt", "a") as arquivo:
    arquivo.write("Maria - 77777-9012\n")

# LER linha por linha
with open("contatos.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

## Por que isso importa?

Programas precisam guardar dados além da memória. Arquivos são a forma mais simples de persistir informações — sem banco de dados, sem complicação.

## Exercícios

- `exercicio_1.py` — cadastro de alunos com notas em arquivo
