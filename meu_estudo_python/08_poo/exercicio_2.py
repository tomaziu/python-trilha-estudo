class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibir_info(self):
        return f"Olá, meu nome é {self.nome} e meu salário é {self.salario}"
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_info(self):
        return f"{super().exibir_info()} e sou gerente do departamento {self.departamento}"

class Atendente(Funcionario):
    def __init__(self, nome, salario, turno):
        super().__init__(nome, salario)
        self.turno = turno

    def exibir_info(self):
        return f"{super().exibir_info()} e trabalho no turno {self.turno}"
    
funcionario1 = Funcionario("Carlos", 3000)
print(funcionario1.exibir_info())

gerente1 = Gerente("Ana", 5000, "Vendas")
print(gerente1.exibir_info())

atendente1 = Atendente("Pedro", 2000, "Noite")
print(atendente1.exibir_info())