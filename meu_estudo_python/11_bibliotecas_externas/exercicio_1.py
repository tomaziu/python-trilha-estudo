# EXERCÍCIO: Consumo de API
# Objetivo: Aprender a buscar dados da internet

import requests

# PASSO 1: Fazer requisição para uma API
# requests.get() busca dados de uma URL
print("═══ Buscando dados da API ═══")
response = requests.get("https://jsonplaceholder.typicode.com/todos")

# PASSO 2: Verificar se deu certo
# status_code 200 = sucesso
if response.status_code == 200:
    print("✓ Conexão bem-sucedida!")
else:
    print(f"✗ Erro: {response.status_code}")

# PASSO 3: Converter resposta para Python
# .json() transforma o texto em lista/dicionário
dados = response.json()
print(f"Total de tarefas: {len(dados)}")

# PASSO 4: Filtrar apenas concluídas
# List comprehension com filtro
concluidas = [todo for todo in dados if todo['completed']]
print(f"Tarefas concluídas: {len(concluidas)}")

# PASSO 5: Mostrar apenas as primeiras 5
print("\n═══ Primeiras 5 Concluídas ═══")
for todo in concluidas[:5]:  # [:5] pega apenas os 5 primeiros
    print(f"  {todo['id']}. {todo['title']}")

# COMO FUNCIONA:
# 1. requests.get(url) → busca dados
# 2. response.json() → converte para Python
# 3. Filtramos com list comprehension
# 4. Mostramos os resultados

# É como um FORMULÁRIO na web:
# Em vez de preencher manualmente,
# o Python preenche e traz os dados!
