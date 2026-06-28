# 09 — Módulos e Biblioteca Padrão

**O que é:** Módulos são arquivos Python que contêm funções e classes prontas. Em vez de escrever tudo do zero, você importa módulos que já resolvem problemas comuns.

## O que está incluído

| Módulo | O que faz | Exemplo |
|--------|-----------|---------|
| `math` | Cálculos matemáticos | `math.sqrt(16)` → `4.0` |
| `random` | Números e escolhas aleatórias | `random.choice(lista)` |
| `datetime` | Datas e horários | `datetime.now()` |
| `os` | Interação com o sistema | `os.path.exists("arq.txt")` |
| `os` | Listar arquivos | `os.listdir("pasta/")` |

## Formas de importar

```python
# Forma 1: importar o módulo inteiro
import math
print(math.sqrt(16))

# Forma 2: importar só o que precisa
from random import choice
print(choice(["a", "b", "c"]))

# Forma 3: importar com apelido (mais comum)
import datetime as dt
print(dt.datetime.now())
```

## Como funciona na prática

```python
import math
import random
import datetime
import os

# math — cálculos
raiz = math.sqrt(25)
pi = math.pi

# random — aleatório
numero = random.randint(1, 10)
cor = random.choice(["azul", "verde", "vermelho"])

# datetime — data atual
agora = datetime.datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))

# os — verificar se arquivo existe
if os.path.exists("dados.txt"):
    print("Arquivo encontrado!")
else:
    print("Arquivo não existe.")
```

## Por que isso importa?

A biblioteca padrão do Python já vem com dezenas de módulos prontos. Usar eles é mais rápido, mais seguro e mais confiável do que escrever do zero.

## Exercícios

| Arquivo | O que você vai fazer | Conceitos aplicados |
|---------|---------------------|---------------------|
| `exercicio_1.py` | Gerar senhas aleatórias e sortear números | `from random import choice, randint`, `from math import sqrt` |
| `exercicio_2.py` | Registrar acessos em arquivo com data e hora | `datetime`, `os.path.exists()`, `os.listdir()`, modos `w` e `a` |

**O que cada exercício ensina:**
- **exercicio_1.py**: Como importar funções específicas com `from...import` e usá-las para gerar dados aleatórios
- **exercicio_2.py**: Como pegar a data/hora atual, verificar se um arquivo existe e listar arquivos da pasta
