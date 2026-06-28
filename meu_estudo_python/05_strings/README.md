# 05 — Strings

**O que é:** Strings são textos. Em Python, você trabalha com strings o tempo todo — nomes, mensagens, dados de entrada. Saber manipular elas é essencial.

## O que está incluído

| Método | O que faz | Exemplo |
|--------|-----------|---------|
| `.upper()` / `.lower()` | Caixa alta/baixa | `"Olá".upper()` → `"OLÁ"` |
| `.strip()` | Remove espaços extras | `" texto ".strip()` → `"texto"` |
| `.split()` | Divide em lista | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.join()` | Junta lista em texto | `", ".join(["a","b"])` → `"a, b"` |
| `.count()` | Conta aparições | `"banana".count("a")` → `3` |
| `.startswith()` / `.endswith()` | Verifica início/fim | `"arquivo.py".endswith(".py")` |
| `f-string` | Insere variáveis no texto | `f"R$ {preco:.2f}"` |
| Fatiamento | Pega pedaços da string | `"Python"[0:3]` → `"Pyt"` |

## Como funciona na prática

```python
# Fatiamento (slicing)
texto = "Python"
print(texto[0:3])    # Pyt (do índice 0 ao 2)
print(texto[::-1])   # nohtyP (inverte a string)

# Métodos úteis
nome = "  Maria Silva  "
print(nome.strip())       # "Maria Silva"
print(nome.strip().lower())  # "maria silva"

# Validação de dados
email = "teste@email.com"
if "@" in email and "." in email:
    print("Email válido!")

# Formatação com f-string
preco = 49.9
print(f"Preço: R$ {preco:.2f}")  # Preço: R$ 49.90
```

## Por que isso importa?

Strings estão em todo lugar: dados de formulários, arquivos CSV, mensagens de erro, URLs. Saber manipular elas é o dia a dia do programador.

## Exercícios

- `exercicio_1.py` — validador de CEP
- `exercicio_2.py` — validador de e-mail
- `exercicio_3.py` — inversão de string
- `exercicio_4.py` — contagem de palavras
