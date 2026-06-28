# 13 — Projeto Final

**O que é:** Projeto integrador que combina todos os tópicos estudados. Aqui você aplica POO, arquivos, tratamento de erros, strings, pandas e boas práticas em um sistema completo.

## Projeto: Gerenciador de Contatos

Um sistema que cadastra, busca, filtra e salva contatos em arquivo CSV.

## Temas combinados

| Tema | Onde aparece no projeto |
|------|------------------------|
| POO | Classe `Contato` com atributos e métodos |
| Arquivos | Leitura e escrita do `contatos.csv` |
| Erros | Validação de entrada com `try/except` |
| Strings | Normalização com `strip()`, `lower()` |
| Pandas | Leitura/escrita do CSV e estatísticas |
| Type hints | Anotações em todos os métodos |
| PEP8 | Formatação profissional |

## Funcionalidades

1. **Cadastrar** — nome, telefone, email, cidade
2. **Listar** — mostra todos os contatos
3. **Buscar** — por nome (parcial)
4. **Filtrar** — por cidade
5. **Salvar/Ler** — persistência em `contatos.csv`
6. **Estatísticas** — total de contatos por cidade

## Estrutura dos arquivos

```
13_projeto_final/
├── contato.py      # Classe Contato
├── main.py         # Menu e fluxo principal
└── contatos.csv    # Dados salvos (gerado automaticamente)
```

## Como rodar

```bash
cd meu_estudo_python/13_projeto_final
python main.py
```
