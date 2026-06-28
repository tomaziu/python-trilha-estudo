# 06 — Tratamento de Erros

**O que é:** Às vezes o programa quebra — o usuário digita uma letra no lugar de um número, divide por zero, tenta abrir um arquivo que não existe. O tratamento de erros faz o programa não travar e mostrar uma mensagem útil.

## O que está incluído

| Conceito | O que faz | Exemplo |
|----------|-----------|---------|
| try | Tenta executar o código | `try:` |
| except | Captura o erro e faz algo | `except ValueError:` |
| finally | Executa sempre, com ou sem erro | `finally:` |
| raise | Lança um erro manualmente | `raise ValueError("Inválido")` |

## Tipos de erro mais comuns

| Erro | Quando acontece |
|------|-----------------|
| `ValueError` | Conversão de tipo falha: `int("abc")` |
| `ZeroDivisionError` | Divisão por zero: `10 / 0` |
| `FileNotFoundError` | Arquivo não encontrado: `open("lixo.txt")` |
| `IndexError` | Índice fora do alcance: `[1,2][5]` |
| `KeyError` | Chave não existe no dict: `{"a":1}["b"]` |

## Como funciona na prática

```python
# Sem tratamento — o programa trava
# numero = int(input("Digite um número: "))
# Se o usuário digitar "abc", o programa crasha

# Com tratamento — o programa continua
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: digite apenas números!")
except ZeroDivisionError:
    print("Erro: não pode dividir por zero!")
finally:
    print("Operação finalizada.")  # sempre executa
```

## Por que isso importa?

Um programa sem tratamento de erros trava na primeira exceção. Com try/except, ele mostra uma mensagem amigável e continua funcionando.

## Exercícios

| Arquivo | O que você vai fazer | Conceitos aplicados |
|---------|---------------------|---------------------|
| `exercicio_1.py` | Criar uma calculadora que nunca trava, mesmo com erros | `try/except`, `ValueError`, `ZeroDivisionError`, `break` |
| `exercicio_2.py` | Cadastrar 3 alunos, calcular médias e salvar em arquivo | Funções, listas, `float()`, `with open()`, escrita em arquivo |

**O que cada exercício ensina:**
- **exercicio_1.py**: Como usar `try/except` para capturar erros e mostrar mensagens amigáveis em vez de o programa travar
- **exercicio_2.py**: Como combinar tratamento de erros com funções e manipulação de arquivos para criar um sistema completo
