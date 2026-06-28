# EXERCÍCIO: Dicionários Dinâmicos
# Objetivo: Aprender dict comprehension e set comprehension

# PASSO 1: Lista de produtos
produtos = [
    {"nome": "Camisa", "preco": 50},
    {"nome": "Calça", "preco": 120},
    {"nome": "Tênis", "preco": 200},
    {"nome": "Boné", "preco": 30},
    {"nome": "Jaqueta", "preco": 250}
]

# PASSO 2: Criar dicionário nome → preço
# {chave: valor for item in lista}
produtos_dict = {p['nome']: f"R${p['preco']}" for p in produtos}
print("═══ Todos os Produtos ═══")
print(produtos_dict)

# PASSO 3: Filtrar apenas caros (acima de R$100)
produtos_caros = {p['nome']: f"R${p['preco']}" for p in produtos if p['preco'] > 100}
print("\n═══ Acima de R$100 ═══")
print(produtos_caros)

# PASSO 4: Set comprehension (remove repetições)
nomes = ["Ana", "João", "ANA", "maria", "João", "MARIA"]
nomes_unicos = {nome.lower() for nome in nomes}  # Converte tudo para minúsculo
print("\n═══ Nomes Únicos ═══")
print(nomes_unicos)

# PASSO 5: Dict comprehension com cálculo
precos = [100, 200, 300, 400, 500]
# Calcula desconto de 10%
com_desconto = {f"R${p}": f"R${p * 0.9:.2f}" for p in precos}
print("\n═══ Com 10% de Desconto ═══")
print(com_desconto)

# COMO FUNCIONA:
# Dict: {p['nome']: p['preco'] for p in produtos}
# Set:  {nome.lower() for nome in nomes}

# DIFERENÇA:
# {} sem : = SET (remove repetições)
# {} com : = DICT (chave: valor)
