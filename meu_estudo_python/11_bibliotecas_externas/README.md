# 11 — Bibliotecas Externas

**O que é:** Bibliotecas que não vêm com o Python padrão, mas são instaladas com `pip`. As mais usadas são **pandas** (análise de dados) e **requests** (chamar APIs).

## O que está incluído

| Biblioteca | O que faz | Exemplo |
|------------|-----------|---------|
| `pip install` | Instala a biblioteca | `pip install pandas` |
| `requests` | Faz requisições HTTP | `requests.get(url)` |
| `pandas` | Manipula dados em tabela | `pd.DataFrame(dados)` |
| `pip freeze` | Lista pacotes instalados | `pip freeze > requirements.txt` |

## Como funciona na prática

```python
# REQUESTS — buscar dados de uma API
import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/users")
dados = resposta.json()

for usuario in dados:
    print(f"{usuario['name']} - {usuario['email']}")

# PANDAS — analisar dados em tabela
import pandas as pd

# Criar DataFrame
notas = {
    "nome": ["Ana", "João", "Maria"],
    "nota": [8.5, 6.0, 9.2]
}
df = pd.DataFrame(notas)

# Filtrar aprovados
aprovados = df[df["nota"] >= 7]
print(aprovados)

# Média das notas
print(f"Média: {df['nota'].mean():.2f}")

# Salvar em CSV
aprovados.to_csv("aprovados.csv", index=False)
```

## Como instalar

```bash
# Ativar ambiente virtual primeiro!
venv\Scripts\Activate.ps1

# Instalar
pip install pandas requests

# Salvar dependências
pip freeze > requirements.txt

# Em outro computador, reinstalar tudo
pip install -r requirements.txt
```

## Por que isso importa?

Pandas e requests são as bibliotecas mais usadas no mercado. Com requests você consome qualquer API; com pandas você analisa qualquer tabela de dados.

## Exercícios

- `exercicio_1.py` — consumo de API com requests
- `exercicio_2.py` — análise de dados com pandas
