# 04 — Funções

**O que é:** Um bloco de código reutilizável. Em vez de copiar e colar o mesmo código várias vezes, você cria uma função e chama ela sempre que precisar.

## O que está incluído

| Conceito | O que faz | Exemplo |
|----------|-----------|---------|
| def | Cria uma função | `def saudacao(nome):` |
| return | Devolve um resultado | `return resultado` |
| Parâmetros | Dados que a função recebe | `def soma(a, b):` |
| Valor padrão | Se o usuário não passar o dado | `def soma(a, b=10):` |
| *args | Aceita N argumentos como tupla | `def soma(*notas):` |
| **kwargs | Aceita N argumentos como dicionário | `def dados(**info):` |
| Escopo | Variáveis dentro da função são locais | Não afetam o resto do programa |

## Como funciona na prática

```python
# Função simples — recebe dados, retorna resultado
def media(notas: list[float]) -> float:
    return sum(notas) / len(notas)

print(media([8, 7, 9]))  # 8.0

# Valor padrão — se não passar nada, usa o default
def saudacao(nome="usuário"):
    return f"Olá, {nome}!"

print(saudacao())         # Olá, usuários!
print(saudacao("Ana"))    # Olá, Ana!

# *args — aceita qualquer quantidade de números
def soma(*numeros):
    return sum(numeros)

print(soma(1, 2, 3))     # 6
print(soma(10, 20))      # 30

# **kwargs — aceita dados nomeados
def criar_perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

criar_perfil(nome="João", idade=25, cidade="SP")
```

## Por que isso importa?

Funções evitam código duplicado, facilitam correção de bugs (muda em um lugar só) e deixam o programa organizado.

## Exercícios

- `exercicio_1.py` — calculadora de média
- `exercicio_2.py` — funções com *args e **kwargs
- `exercicio_3.py` — escopo local vs global
