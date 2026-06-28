# 12 — Boas Práticas

**O que é:** Regras e convenções que tornam seu código profissional, legível e fácil de manter. Não afetam a execução, mas fazem diferença no mundo real.

## O que está incluído

| Tema | O que é | Exemplo |
|------|---------|---------|
| PEP8 | Guia de estilo oficial | Espaços ao redor de `=`, `+` |
| Type hints | Anotação de tipos | `def soma(a: int) -> int:` |
| Virtualenv | Ambiente isolado por projeto | `python -m venv venv` |
| requirements.txt | Lista de dependências | `pip freeze > requirements.txt` |

## PEP8 — Regras essenciais

```python
# ❌ ERRADO — sem espaços, nomes bagunçados
def soma(a,b):
    resultado=a+b
    return resultado

# ✅ CERTO — espaços, snake_case, indentação
def soma(a, b):
    resultado = a + b
    return resultado
```

**Regras rápidas:**
- Espaço antes e depois de `=`, `+`, `-`, `==`, etc.
- Espaço depois de cada `,`
- 4 espaços de indentação (nunca tabs)
- `snake_case` para variáveis/funções, `PascalCase` para classes
- Máximo 79 caracteres por linha

## Type hints — Deixe claro o tipo

```python
# Sem type hints — não sei o que a função retorna
def media(notas):
    return sum(notas) / len(notas)

# Com type hints — claro e autoexplicativo
def media(notas: list[float]) -> float:
    return sum(notas) / len(notas)
```

**Tipos mais usados:**
```python
nome: str = "João"
idade: int = 25
altura: float = 1.75
ativo: bool = True
notas: list[float] = [8.0, 7.5]
dados: dict[str, int] = {"a": 1}
```

## Virtualenv — Isole seus projetos

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\Activate.ps1

# Ativar (Mac/Linux)
source venv/bin/activate

# Desativar
deactivate
```

**Por que usar?** Se o Projeto A precisa de pandas 1.5 e o Projeto B de pandas 2.0, o virtualenv evita conflito entre eles.

## Por que isso importa?

Código sem boas práticas funciona, mas é difícil de ler, manter e compartilhar. PEP8 + type hints + virtualenv são o mínimo esperado de um desenvolvedor profissional.

## Exercícios

| Arquivo | O que você vai fazer | Conceitos aplicados |
|---------|---------------------|---------------------|
| `exercicio_1.py` | Escrever código formatado seguindo PEP8 | snake_case, PascalCase, espaços, indentação, type hints |
| `exercicio_2.py` | Criar calculadora de IMC com funções organizadas | `def` com type hints, validação, `if __name__ == "__main__"` |

**O que cada exercício ensina:**
- **exercicio_1.py**: As regras de formatação do PEP8 (espaços, nomes, indentação) e como aplicá-las em código real
- **exercicio_2.py**: Como usar type hints em funções e classes para deixar o código claro e autoexplicativo
