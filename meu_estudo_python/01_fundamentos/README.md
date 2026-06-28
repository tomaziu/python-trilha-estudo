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

- `exercicio_1.py` — calculadora básica com input do usuário
- `exercicio_2.py` — conversor de temperaturas
- `exercicio_3.py` — dados pessoais com f-strings
