email = input("Digite o email: ")

if "@" in email and (email.endswith(".com") or email.endswith(".com.br")):
    print("Email válido")
    email_formatado = email.split("@")
    print(f"Nome do usuário: {email_formatado[1]}")
else:
    print("Email inválido! Digite um email válido.")
