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

    def to_dict(self) -> dict:
        """Converte para dicionário (para salvar no CSV)"""
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "cidade": self.cidade
        }

    @staticmethod  # Método que não precisa de self
    def from_dict(dados: dict) -> "Contato":
        """Cria Contato a partir de um dicionário"""
        return Contato(
            dados["nome"],
            dados["telefone"],
            dados["email"],
            dados["cidade"]
        )

# COMO FUNCIONA:
# contato = Contato("ana", "12345", "ana@email.com", "são paulo")
# contato.nome → "Ana" (formato title)
# contato.email → "ana@email.com" (formato lower)
# contato.cidade → "São Paulo" (formato title)
# str(contato) → "Ana | 12345 | ana@email.com | São Paulo"
