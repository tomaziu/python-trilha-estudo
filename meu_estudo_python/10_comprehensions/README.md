# 10 — Comprehensions

**O que é:** Uma forma curta e rápida de criar listas, dicionários e sets em uma única linha. Substitui loops de 3-4 linhas por uma linha só.

## O que está incluído

| Tipo | Sintaxe | Exemplo |
|------|---------|---------|
| List comprehension | `[expr for x in lista]` | `[x*2 for x in nums]` |
| Com filtro | `[expr for x in lista if cond]` | `[x for x in nums if x > 5]` |
| Dict comprehension | `{chave: valor for x in lista}` | `{n: n**2 for n in nums}` |
| Set comprehension | `{expr for x in lista}` | `{x.lower() for x in nomes}` |

## Antes vs Depois

```python
# SEM comprehension (4 linhas)
dobros = []
for x in [1, 2, 3, 4, 5]:
    if x % 2 == 0:
        dobros.append(x * 2)

# COM comprehension (1 linha)
dobros = [x * 2 for x in [1, 2, 3, 4, 5] if x % 2 == 0]
```

## Como funciona na prática

```python
notas = [8, 5, 9, 3, 7, 10, 2]

# Filtrar aprovados (nota >= 7)
aprovados = [n for n in notas if n >= 7]
print(aprovados)  # [8, 9, 7, 10]

# Criar dicionário nota → situação
situacoes = {n: "OK" if n >= 7 else "FALHOU" for n in notas}
print(situacoes)  # {8: 'OK', 5: 'FALHOU', ...}

# Set de nomes em minúsculo
nomes = ["ANA", "João", "MARIA"]
unicos = {n.lower() for n in nomes}
print(unicos)  # {'ana', 'joão', 'maria'}
```

## Dica importante

```python
# Diferença entre {} para set e dict:
nums = {1, 2, 3}        # SET (sem dois-pontos)
pares = {n: n*2 for n in [1,2,3]}  # DICT (com dois-pontos)
```

## Por que isso importa?

Comprehensions tornam o código mais curto, mais rápido e mais "Pythonic". É um diferencial que mostra domínio da linguagem.

## Exercícios

- `exercicio_1.py` — listas filtradas com comprehension
- `exercicio_2.py` — dicionários dinâmicos
