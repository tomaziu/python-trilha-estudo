# EXERCÍCIO: Validador de E-mail
# Objetivo: Aprender validação com 'in' e endswith()

# PASSO 1: Pedir o email ao usuário
email = input("Digite o email: ")

# PASSO 2: Verificar se é válido
# "@" in email → verifica se tem @ no email
# endswith() → verifica se termina com algo
if "@" in email and (email.endswith(".com") or email.endswith(".com.br")):
    print("✓ Email válido!")
    
    # PASSO 3: Separar usuário e domínio
    # split("@") divide onde tem @
    # "ana@email.com" vira ["ana", "email.com"]
    partes = email.split("@")
    print(f"Usuário: {partes[0]}")
    print(f"Domínio: {partes[1]}")
else:
    print("✗ Email inválido!")
    print("  O email deve conter @ e terminar com .com ou .com.br")

# COMO FUNCIONA:
# email = "ana@email.com"
# "@" in "ana@email.com" = True (tem @)
# "ana@email.com".endswith(".com") = True
# Resultado: válido!

# EXEMPLOS:
# "ana@email.com" → válido
# "ana@email.com.br" → válido
# "anaemail.com" → inválido (não tem @)
# "ana@" → inválido (não termina com .com)
