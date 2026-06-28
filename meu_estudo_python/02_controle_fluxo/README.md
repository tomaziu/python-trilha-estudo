# 02 — Controle de Fluxo

**O que é:** Decide o que o programa faz com base em condições (se isso, faça aquilo) e repete ações com laços (faça isso várias vezes).

## O que está incluído

| Conceito | O que faz | Exemplo |
|----------|-----------|---------|
| if/elif/else | Escolhe um caminho dependendo da condição | `if idade >= 18:` |
| for | Repete algo para cada item de uma lista | `for i in range(5):` |
| while | Repete enquanto uma condição for verdadeira | `while numero != 0:` |
| break | Para o laço no meio | `if numero == 0: break` |
| continue | Pula para a próxima repetição | `if numero < 0: continue` |

## Como funciona na prática

```python
# Condicional — o programa escolhe um caminho
nota = 7.5
if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Laço for — repete N vezes
for i in range(1, 6):  # i vai de 1 a 5
    print(f"Tabuada de 3: {i} x 3 = {i * 3}")

# Laço while — repete até algo acontecer
senha = ""
while senha != "python123":
    senha = input("Digite a senha: ")
print("Acesso liberado!")
```

## Por que isso importa?

Todo programa precisa tomar decisões e repetir tarefas. Sem controle de fluxo, o Python só executaria linha por linha, sem lógica.

## Exercícios

| Arquivo | O que você vai fazer | Conceitos aplicados |
|---------|---------------------|---------------------|
| `exercicio_1.py` | Criar um gerador de tabuada que continua rodando até o usuário querer parar | `while True`, `try/except`, `for` com `range()`, `break`, operador `%` |

**O que o exercício ensina:**
- **Loop while True**: Como criar um loop que repete infinitamente até dar `break`
- **Tratamento de erros**: Como usar `try/except` para o programa não travar quando o usuário digita errado
- **Loop for**: Como usar `range(1, 11)` para gerar números de 1 a 10
- **Operador módulo (%)**: Como verificar se um número é par (resto da divisão por 2 = 0)
- **Métodos de string**: `.strip()` para remover espaços e `.lower()` para converter para minúsculo
