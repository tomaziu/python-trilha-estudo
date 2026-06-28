# 08 — Programação Orientada a Objetos (POO)

**O que é:** Uma forma de organizar o código criando "objetos" que agrupam dados e funcionalidades juntos. Em vez de ter variáveis soltas e funções separadas, você cria uma classe que representa algo do mundo real.

## O que está incluído

| Conceito | O que faz | Exemplo |
|----------|-----------|---------|
| class | Cria uma nova classe (molde) | `class Pessoa:` |
| `__init__` | Método que roda ao criar o objeto | `def __init__(self, nome):` |
| self | Referência ao próprio objeto | `self.nome = nome` |
| Método | Função dentro da classe | `def exibir(self):` |
| Herança | Uma classe herda de outra | `class Aluno(Pessoa):` |
| super() | Chama o método da classe pai | `super().__init__(nome)` |
| `__str__` | O que aparece ao fazer `print(obj)` | `return f"Nome: {self.nome}"` |

## Como funciona na prática

```python
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"{self.nome}, {self.idade} anos"


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, nota: float) -> None:
        super().__init__(nome, idade)  # chama o __init__ do Pai
        self.nota = nota

    def situacao(self) -> str:
        return "Aprovado" if self.nota >= 7 else "Reprovado"


# Criando objetos
p1 = Pessoa("Carlos", 30)
a1 = Aluno("Ana", 20, 8.5)

print(p1)        # Carlos, 30 anos
print(a1)        # Ana, 20 anos
print(a1.situacao())  # Aprovado
```

## Por que isso importa?

POO organiza código grande em partes lógicas. Em vez de ter 50 funções soltas, você tem classes que representam "Pessoa", "Produto", "ContaBancária" — cada uma com seus próprios dados e ações.

## Exercícios

| Arquivo | O que você vai fazer | Conceitos aplicados |
|---------|---------------------|---------------------|
| `exercicio_1.py` | Criar uma classe Pessoa com nome e idade | `class`, `__init__`, `self`, métodos |
| `exercicio_2.py` | Criar hierarquia: Funcionário → Gerente e Atendente | Herança, `super()`, sobrescrita de métodos |
| `exercicio_3.py` | Criar uma Playlist que pode ser somada com outra | `__str__`, `__len__`, `__add__` (métodos mágicos) |

**O que cada exercício ensina:**
- **exercicio_1.py**: O básico de POO — como criar uma classe, o que é `__init__` e `self`, e como chamar métodos
- **exercicio_2.py**: Como uma classe pode HERDAR de outra e como usar `super()` para reutilizar código
- **exercicio_3.py**: Como usar métodos especiais para fazer objetos funcionarem com operadores como `+` e `print()`
