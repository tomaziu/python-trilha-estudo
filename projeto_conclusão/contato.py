class Contato:
    def __init__(self, nome="", telefone=0, email="", cidade=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cidade = cidade
    
    def __str__(self):
        return (
        f"{'Nome:':<10} {self.nome}\n"
        f"{'Telefone:':<10} {self.telefone}\n"
        f"{'E-mail:':<10} {self.email}\n"
        f"{'Cidade:':<10} {self.cidade}"
    )

