# EXERCÍCIO: Validador de CEP
# Objetivo: Aprender validação com len() e fatiamento

# PASSO 1: Pedir o CEP ao usuário
cep = input("Digite o CEP (somente números): ")

# PASSO 2: Verificar se tem 8 dígitos
# len() retorna o tamanho da string
if len(cep) == 8:
    print("✓ CEP válido!")
    
    # PASSO 3: Formatar o CEP (12345678 → 12345-678)
    # cep[0:5] pega os 5 primeiros dígitos
    # cep[5:8] pega os 3 últimos dígitos
    cep_formatado = cep[0:5] + "-" + cep[5:8]
    print(f"CEP formatado: {cep_formatado}")
else:
    print("✗ CEP inválido! Digite exatamente 8 números.")   

# COMO FUNCIONA:
# Usuário digita: 12345678
# len("12345678") = 8 → válido!
# cep[0:5] = "12345"
# cep[5:8] = "678"
# "12345" + "-" + "678" = "12345-678"

# SE DIGITAR ERRADO:
# "12345" → len = 5 → inválido
# "123456789" → len = 9 → inválido
