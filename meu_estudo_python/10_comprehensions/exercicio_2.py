produtos = [
    {"nome": "Camisa", "preco": 50},
    {"nome": "Calça", "preco": 120},
    {"nome": "Tênis", "preco": 200},
    {"nome": "Boné", "preco": 30}
]
    
produtos_comprendidos = {produto['nome']: f"R${produto['preco']}" for produto in produtos}

produtos_comprendidos_100 = {produto['nome']: f"R${produto['preco']}" for produto in produtos if produto['preco'] > 100}


print(produtos_comprendidos)
print(produtos_comprendidos_100)