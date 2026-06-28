# 03 — Estruturas de Dados

**O que é:** Formas de guardar vários dados ao mesmo tempo. Em vez de criar 100 variáveis separadas, você guarda tudo em uma estrutura organizada.

## O que está incluído

| Estrutura | O que é | Quando usar | Exemplo |
|-----------|---------|-------------|---------|
| Lista `[ ]` | Coleção ordenada, pode mudar | Guardar vários itens do mesmo tipo | `notas = [8, 7, 9]` |
| Tupla `( )` | Coleção ordenada, NÃO pode mudar | Dados fixos como coordenadas | `coord = (10, 20)` |
| Dicionário `{ }` | Pares chave-valor | Dados com nome/valor | `pessoa = {"nome": "Ana"}` |
| Set `{ }` | Coleção sem repetição | Remover duplicatas | `nums = {1, 2, 3}` |

## Como funciona na prática

```python
# LISTA — ordenada, pode alterar
notas = [8, 7, 9, 6, 10]
notas.append(7)          # adiciona no final
print(notas[0])          # primeiro elemento: 8
print(len(notas))        # quantos itens: 6

# TUPLA — não muda depois de criada
ponto = (5, 10)
# ponto[0] = 3  # ERRO! tupla não altera

# DICIONÁRIO — cada dado tem um nome (chave)
aluno = {
    "nome": "Carlos",
    "nota": 8.5,
    "aprovado": True
}
print(aluno["nome"])     # Carlos
aluno["cidade"] = "SP"   # adiciona novo campo

# SET — remove repetições automaticamente
numeros = [1, 2, 2, 3, 3, 3]
unicos = set(numeros)
print(unicos)  # {1, 2, 3}
```

## Por que isso importa?

Na vida real, você nunca trabalha com um único dado. Um cadastro tem nome, telefone, email... estruturas de dados organizam tudo isso.

## Exercícios

| Arquivo | O que você vai fazer | Conceitos aplicados |
|---------|---------------------|---------------------|
| `exercicio_1.py` | Criar uma agenda de contatos que permite cadastrar, pesquisar e contar nomes únicos | Listas, `append()`, operador `in`, `set()`, `len()`, loops `for` e `while` |

**O que o exercício ensina:**
- **Listas**: Como criar uma lista vazia e adicionar itens com `append()`
- **Busca em lista**: Como usar o operador `in` para verificar se um item existe
- **Loop while**: Como criar um menu de busca que continua até o usuário querer parar
- **Set (conjunto)**: Como usar `set()` para remover duplicatas automaticamente
- **len()**: Como contar quantos itens existem em uma lista
