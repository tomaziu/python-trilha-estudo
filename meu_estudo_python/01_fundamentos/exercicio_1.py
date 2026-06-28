# EXERCÍCIO 1: Dados Pessoais
# Objetivo: Aprender a criar variáveis e usar f-strings

# PASSO 1: Criar variáveis para guardar os dados
# O nome do lado esquerdo é o que você escolhe para guardar o dado
# O lado direito é o valor que será guardado
seu_nome = "Carlos"        # str = texto (sempre entre aspas)
sua_idade = 25             # int = número inteiro (sem aspas)
sua_cidade = "São Paulo"   # str = texto

# PASSO 2: Usar f-string para mostrar os dados na tela
# O "f" antes das aspas ativa a f-string
# Dentro de { } colocamos o nome da variável
print(f'Olá, meu nome é {seu_nome}, tenho {sua_idade} anos e moro em {sua_cidade}.')

# COMO FUNCIONA:
# O Python substitui {seu_nome} pelo valor "Carlos"
# O Python substitui {sua_idade} pelo valor 25
# O Python substitui {sua_cidade} pelo valor "São Paulo"
# Resultado: Olá, meu nome é Carlos, tenho 25 anos e moro em São Paulo.
