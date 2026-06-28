# EXERCÍCIO: Classes Pessoa e Animal
# Objetivo: Aprender os fundamentos de POO

# PASSO 1: Criar uma classe
# class é um MOLDE para criar objetos
# Pessoa é o nome da classe (PascalCase - maiúscula)
class Pessoa:
    
    # __init__ é o CONSTRUTOR - roda ao criar o objeto
    # self = o próprio objeto que está sendo criado
    # nome e idade são os dados que recebemos
    def __init__(self, nome, idade):
        self.nome = nome    # Guarda o nome no objeto
        self.idade = idade  # Guarda a idade no objeto
    
    # Método = função dentro da classe
    # self dá acesso aos dados do objeto
    def apresentar(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos."
    
    def aniversario(self):
        self.idade += 1  # Aumenta a idade em 1
        return f"🎉 {self.nome} fez aniversário! Agora tem {self.idade} anos."

# PASSO 2: Criar objetos (instâncias da classe)
# Cada objeto é uma "cópia" independente do molde
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)
pessoa3 = Pessoa("Pedro", 22)

# PASSO 3: Usar os métodos
print(pessoa1.apresentar())  # João tem seus próprios dados
print(pessoa2.apresentar())  # Maria tem seus próprios dados
print()

# Chamando aniversário
print(pessoa1.aniversario())
print(f"Idade atual: {pessoa1.idade}")

# COMO FUNCIONA:
# Pessoa("João", 25) cria um objeto com:
#   self.nome = "João"
#   self.idade = 25
# 
# pessoa1.apresentar() usa os dados DELE:
#   return f"Olá, eu sou João e tenho 25 anos."

# É como uma FÁBRICA:
# Classe = fábrica (o molde)
# Objeto = produto (o que a fábrica cria)
# Cada produto pode ser diferente!
