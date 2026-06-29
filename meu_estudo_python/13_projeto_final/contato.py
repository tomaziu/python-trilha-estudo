# CLASSE CONTATO - Modelo para o Gerenciador
# Conceitos: POO, métodos especiais, type hints

class Contato:
    """Classe que representa um contato"""
    
    def __init__(self, nome: str, telefone: str, email: str, cidade: str) -> None:
        """Construtor - inicializa o contato"""
        # .strip() remove espaços extras das pontas
        # .title() coloca maiúscula no início de cada palavra
        self.nome = nome.strip().title()
        self.telefone = telefone.strip()
        # .lower() converte para minúsculo (para emails)
        self.email = email.strip().lower()
        self.cidade = cidade.strip().title()

    def __str__(self) -> str:
        """Define o que aparece ao fazer print(contato)"""
        return f"{self.nome} | {self.telefone} | {self.email} | {self.cidade}"

# contato = Contato("ana", "12345", "ana@email.com", "são paulo")
# contato.nome → "Ana" (formato title)
# contato.email → "ana@email.com" (formato lower)
# contato.cidade → "São Paulo" (formato title)
