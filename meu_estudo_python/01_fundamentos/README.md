# 01 — Fundamentos

**O que é:** A base de qualquer programa em Python. Aqui você aprende a criar variáveis, armazenar dados e fazer operações simples.

## O que está incluído

| Conceito | O que faz | Exemplo |
|----------|-----------|---------|
| Variáveis | Guardam um valor com um nome | `nome = "João"` |
| Tipos | Definem o tipo do dado (texto, número, verdadeiro/falso) | `int`, `str`, `float`, `bool` |
| Operadores | Fazem cálculos e comparações | `+`, `-`, `*`, `/`, `==`, `>` |
| f-strings | Inserem variáveis dentro de texto | `f"Olá, {nome}"` |
| input() | Pedem dados ao usuário pelo terminal | `idade = int(input("Idade: "))` |

## Como funciona na prática

```python
# Uma variável é como uma caixa com um nome
nome = "Maria"          # str (texto)
idade = 25              # int (número inteiro)
altura = 1.65           # float (número com casa decimal)
estudante = True        # bool (verdadeiro ou falso)

# f-string coloca variáveis dentro de uma frase
print(f"Nome: {nome}, Idade: {idade}")

# input() sempre retorna texto, por isso convertemos com int()
ano = int(input("Digite o ano de nascimento: "))
print(f"Você nasceu em {2026 - ano}")
```

## Por que isso importa?

Sem variáveis e tipos, não existe programa. Tudo em Python começa aqui — desde um script simples até um sistema completo.

## Exercícios

| Arquivo | O que você vai fazer | Conceitos aplicados |
|---------|---------------------|---------------------|
| `exercicio_1.py` | Criar variáveis com dados pessoais e mostrar na tela | Variáveis `str` e `int`, f-strings com `{variavel}` |
| `exercicio_2.py` | Fazer operações matemáticas (soma, subtração, multiplicação) | Operadores `+`, `-`, `*`, `/`, `//`, `%` |
| `exercicio_3.py` | Pedir números ao usuário e calcular a soma | `input()`, conversão com `int()`, por que sempre retorna texto |

**O que cada exercício ensina:**
- **exercicio_1.py**: Como guardar dados em variáveis e usar f-strings para mostrar texto com valores dinâmicos
- **exercicio_2.py**: Todos os operadores matemáticos do Python e a diferença entre `/` (divisão normal) e `//` (divisão inteira)
- **exercicio_3.py**: Por que `input()` sempre retorna texto e como converter para número com `int()`
