# EXERCÍCIO: Herança com Funcionário
# Objetivo: Aprender herança e sobrescrita de métodos

# PASSO 1: Criar classe PAI (base)
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibir_info(self):
        return f"Nome: {self.nome} | Salário: R${self.salario}"

# PASSO 2: Criar classe FILHA (herda de Funcionario)
class Gerente(Funcionario):
    # __init__ próprio do Gerente
    def __init__(self, nome, salario, departamento):
        # super() chama o __init__ da classe PAI
        super().__init__(nome, salario)
        self.departamento = departamento  # Atributo NOVO

    # SOBRESCRITA: método igual ao pai, mas com código diferente
    def exibir_info(self):
        # super().exibir_info() usa o método do pai
        info_pai = super().exibir_info()
        return f"{info_pai} | Depto: {self.departamento}"

# OUTRA classe filha
class Atendente(Funcionario):
    def __init__(self, nome, salario, turno):
        super().__init__(nome, salario)
        self.turno = turno

    def exibir_info(self):
        info_pai = super().exibir_info()
        return f"{info_pai} | Turno: {self.turno}"

# PASSO 3: Criar objetos e testar
print("═══ Funcionário Comum ═══")
func1 = Funcionario("Carlos", 3000)
print(func1.exibir_info())

print("\n═══ Gerente ═══")
gerente1 = Gerente("Ana", 5000, "Vendas")
print(gerente1.exibir_info())

print("\n═══ Atendente ═══")
aten1 = Atendente("Pedro", 2000, "Noite")
print(aten1.exibir_info())

# COMO FUNCIONA A HERANÇA:
# Gerente HERDA tudo de Funcionario (nome, salario, exibir_info)
# Mas ADICIONA departamento
# E MUDA como exibir_info funciona

# É como uma FAMÍLIA:
# Pai = Funcionario (tem nome, salário)
# Filho = Gerente (herda nome, salário + ganha departamento)
# Filho = Atendente (herda nome, salário + ganha turno)
