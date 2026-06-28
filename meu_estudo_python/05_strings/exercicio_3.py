cep = input("Digite o CEP (somente números): ")

if len(cep) == 8:
    print("CEP válido")
    cep_formatado = (cep[0:5] + "-" + cep[5:8])
    print(f"CEP formatado: {cep_formatado}")
else:
    print("CEP inválido! Digite um CEP com 8 dígitos.")   

