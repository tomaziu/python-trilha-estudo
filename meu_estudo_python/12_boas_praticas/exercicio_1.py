def calcula_media(notas: list[float]) -> float:
    total = 0
    for n in notas:
        total = total + n
    media = total / len(notas)
    return media


class Aluno:
    
    def __init__(self, nome: str, notas: list[float]) -> None:
        self.nome = nome
        self.notas = notas
   
    def exibir(self) -> None:
        m = calcula_media(self.notas)
        print(f"Aluno: {self.nome} Média: {m}")