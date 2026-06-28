class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
pessoa1 = Pessoa("João", 25)
print(pessoa1.apresentar())

pessoa2 = Pessoa("Maria", 30)
print(pessoa2.apresentar())