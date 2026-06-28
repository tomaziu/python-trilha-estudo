# EXERCÍCIO: Código com PEP8
# Objetivo: Aprender boas práticas de formatação

# ═══ ANTES (código bagunçado) ═══
# def soma(a,b):
#     resultado=a+b
#     return resultado

# ═══ DEPOIS (com PEP8) ═══
# Type hints indicam o tipo de cada dado
def calcula_media(notas: list[float]) -> float:
    """Calcula a média de uma lista de notas"""
    total = 0.0
    for n in notas:
        total = total + n  # Espaço antes e depois de =
    media = total / len(notas)
    return media


class Aluno:
    """Classe que representa um aluno"""
    
    def __init__(self, nome: str, notas: list[float]) -> None:
        self.nome = nome
        self.notas = notas
   
    def exibir(self) -> None:
        """Exibe nome e média"""
        m = calcula_media(self.notas)
        print(f"Aluno: {self.nome} | Média: {m:.2f}")


# ═══ TESTANDO ═══
aluno1 = Aluno("Ana", [8.5, 7.0, 9.0])
aluno1.exibir()

aluno2 = Aluno("Pedro", [5.0, 6.5, 4.0])
aluno2.exibir()

# ═══ REGRAS PEP8 ═══
# ✓ Espaço antes/depois de =, +, -, ==
# ✓ Espaço depois de cada vírgula
# ✓ 4 espaços de indentação (nunca tabs)
# ✓ snake_case para variáveis/funções
# ✓ PascalCase para classes (Aluno, Pessoa)
# ✓ Máximo 79 caracteres por linha
# ✓ Type hints: def soma(a: int) -> int:

# COMO FUNCIONA:
# ANTES: resultado=a+b     (difícil de ler)
# DEPOIS: resultado = a + b (fácil de ler)
